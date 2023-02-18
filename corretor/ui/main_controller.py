#------------------------------------------------------------------------------#
'''Define main interface controller'''

from pathlib   import Path
from functools import partial
from typing    import Callable

from PySide6.QtCore    import QRegularExpression, QUrl
from PySide6.QtWidgets import (QMainWindow,
                               QApplication,
                               QFileDialog,
                               QMessageBox)
from PySide6.QtGui     import (QRegularExpressionValidator,
                               QAction,
                               QDesktopServices)

import ena_param as ep

from ui.main_model       import MainModel
from ui.edit_keys_dialog import EditKeysDialog
from ui.progress_dialog  import ProgressDialog
from ui.help_window      import HelpWindow
from ui.show_names       import show_names

#------------------------------------------------------------------------------#
class MainController:
    '''Main interface controller class'''

    #--------------------------------------------------------------------------#
    def __init__(self, window: QMainWindow) -> None:
        '''Initialise main interface controller instance'''

        self.win = window
        self.ui  = window.ui

        self.last_dir              = ep.HOME
        self.suggested_annotations = ''
        self.suggested_results     = ''
        self.keys_fname            = ''

        self.uimodel = MainModel()

        self.start_line_edits()
        self.connectSignalsAndSlots()

    #--------------------------------------------------------------------------#
    def start_line_edits(self) -> None:
        '''Initialise line edit widgets'''

        k_model = self.uimodel.keys_model

        self.ui.lineEditKeys.setFont     (k_model.font)
        self.ui.lineEditKeys.setInputMask(k_model.mask)
        self.ui.lineEditKeys.setValidator(k_model.validator(self.win))
        self.ui.lineEditKeys.setText     (k_model.keys)

        regex     = QRegularExpression           ('[A-Z][1-9]')
        validator = QRegularExpressionValidator  (regex, self.win)
        self.ui.lineEditNameFistName.setFont     (k_model.font)
        self.ui.lineEditNameFistName.setInputMask('>AD')
        self.ui.lineEditNameFistName.setValidator(validator)

    #--------------------------------------------------------------------------#
    def connectSignalsAndSlots(self) -> None:
        '''Initialise callbacks'''

        ui    = self.ui
        model = self.uimodel

        ui.action_Run  .triggered.connect(self.run)
        ui.pushButtonRun .clicked.connect(self.run)
        ui.pushButtonExit.clicked.connect(self.exit)

        ui.action_Exit.triggered.connect(self.exit)

        ui.action_Keys_Open  .triggered.connect(self.open_keys)
        ui.action_Keys_Save  .triggered.connect(self.save_keys)
        ui.action_Keys_Saveas.triggered.connect(self.saveas_keys)

        ui.action_About.triggered.connect(self.about)
        ui.action_Help .triggered.connect(self.help)

        for yy in model.keys_model.get_ena_years():
            action = QAction(f'ENA {yy}', self.win)
            action.triggered.connect(partial(self.set_ena_keys, yy))
            ui.menuKeys.addAction(action)

        ui.pushButtonModelOpen.clicked.connect(self.open_model)

        ui.pushButtonKeysEdit         .clicked.connect(self.edit_keys)
        ui.lineEditKeys       .editingFinished.connect(self.parse_keys)
        ui.spinBoxMinimumCorrects.valueChanged.connect(self.set_minimum)

        ui.pushButtonExamsOpen.clicked.connect(self.open_exams)

        ui.pushButtonNamesOpen         .clicked.connect(self.open_names)
        ui.pushButtonNamesShow         .clicked.connect(self.show_names)
        ui.pushButtonNamesRemove       .clicked.connect(self.remove_names)
        ui.lineEditNameFistName.editingFinished.connect(self.set_first_cell)

        ui.pushButtonOutputResultsChoose    .clicked.connect(self.choose_results)
        ui.pushButtonOutputAnnotationsChoose.clicked.connect(self.choose_annotations)

        def show_connect(widget, function: Callable[[None],None]) -> None:
            widget.clicked.connect(partial(self.show, function))

        show_connect(ui.pushButtonModelShow,       model.get_model_pdf      )
        show_connect(ui.pushButtonKeysShow,        model.get_keys_pdf       )
        show_connect(ui.pushButtonExamsShow,       model.get_exams_pdf      )
        show_connect(ui.pushButtonResultsShow,     model.get_results_xlsx   )
        show_connect(ui.pushButtonAnnotationsShow, model.get_annotations_pdf)

    #--------------------------------------------------------------------------#
    def update(self) -> None:
        '''Update window widgets'''

        has_model   = self.uimodel.has_model
        has_exams   = self.uimodel.has_exams
        has_names   = self.uimodel.has_names
        has_results = self.uimodel.has_results
        has_annot   = self.uimodel.has_annot

        self.ui.pushButtonModelShow.setEnabled(has_model)
        self.ui.labelModelFileName .setEnabled(has_model)
        self.ui.pushButtonKeysShow .setEnabled(has_model)

        self.ui.pushButtonExamsShow.setEnabled(has_exams)
        self.ui.labelExamsFileName .setEnabled(has_exams)

        self.ui.pushButtonNamesShow  .setEnabled(has_names)
        self.ui.pushButtonNamesRemove.setEnabled(has_names)
        self.ui.labelNamesFileName   .setEnabled(has_names)

        self.ui.labelOutputResultsFileName    .setEnabled(has_results)
        self.ui.labelOutputAnnotationsFileName.setEnabled(has_annot)

        done = self.uimodel.done

        self.ui.pushButtonResultsShow    .setEnabled(done)
        self.ui.pushButtonAnnotationsShow.setEnabled(done)

        ready = self.uimodel.ready_to_run()
        self.ui.labelCorrection.setEnabled(ready)
        self.ui.action_Run     .setEnabled(ready)
        self.ui.pushButtonRun  .setEnabled(ready)

        num_exams = self.uimodel.num_exams
        num_names = self.uimodel.num_names

        if done:
            message = 'Provas corrigidas'

        elif self.uimodel.has_conflict():
            message = (
                f'Atenção: A quantidade de respostas ({num_exams}) '
                f'não coincide com a quantidade de candidatos ({num_names})'
            )

        elif has_exams:
            message = f'Corrigir {num_exams} provas'

        else:
            message = 'Corrigir provas'

        self.ui.labelCorrection.setText(message)

    #--------------------------------------------------------------------------#
    def exit(self) -> None:
        '''Terminate application execution'''

        QApplication.quit()

    #--------------------------------------------------------------------------#
    def run(self) -> None:
        '''Execute the correction'''

        if self.uimodel.has_conflict():
            ans = QMessageBox.question(
                self.win,
                'Conflito',
                ('A quantidade de folhas respostas não coincide '
                 'com a quantidade de candidatos.'
                 '\n\n'
                 'Corrigir mesmo assim?'
                )
            )

            if ans == QMessageBox.No:
                return

        progress = ProgressDialog(self.win, ep.TITLE+' - Correção')

        try:
            finished = self.uimodel.run(progress)

        except IOError as er:
            self.error_box(
                'Erro salvando os arquivos',
                ('Não foi possível salvar algum dos arquivos!'
                 f'\n\n{str(er)}'
                )
            )

        else:
            msg = QMessageBox(self.win)
            msg.setIcon(QMessageBox.Information)

            if finished:
                msg.setWindowTitle( ep.TITLE+' - Conclusão')
                msg.setText(        ep.TITLE+': Correção Concluída' + ' '*25)
            else:
                msg.setWindowTitle( ep.TITLE+' - Conclusão')
                msg.setText(        ep.TITLE+': Correção Cancelada' + ' '*25)

            msg.show()

        self.update()

    #--------------------------------------------------------------------------#
    def about(self) -> None:
        '''Show about dialog box'''

        QMessageBox.about(self.win, ep.TITLE+' - Sobre', ep.ABOUT)

    #--------------------------------------------------------------------------#
    def help(self) -> None:
        '''Show help window'''

        HelpWindow(self.win)

    #--------------------------------------------------------------------------#
    def open_model(self) -> None:
        '''Open PDF file with model'''

        fname = self.get_open_fname(
            'Selecione o modelo da folha de respostas',
            'pdf'
        )

        if not fname: return

        self.last_dir = Path(fname).parent

        message = ''

        try:
            self.uimodel.set_model(fname)

        except ValueError as er:
            message = str(er)

        except (
            IOError,
            FileNotFoundError,
            RuntimeError
        ) as er:
            message = (
                f'Não foi possível ler o arquivo com o modelo!\n\n'
                f'Mensagem: {str(er)}'
            )

        else:
            self.ui.labelModelFileName.setText(fname)
            self.update()

        if message:
            self.error_box('Erro lendo o modelo', message)

    #--------------------------------------------------------------------------#
    def open_exams(self) -> None:
        '''Open PDF file with exams'''

        fname = self.get_open_fname(
            'Selecione o arquivo com as respostas para serem corrigidas',
            'pdf'
        )

        if not fname: return

        self.last_dir = Path(fname).parent

        accept = self.load_names_or_exams(
            partial(self.uimodel.set_exams, fname),
            'as respostas'
            )

        if accept:
            self.suggested_annotations = fname[:-4] + '-anotacoes.pdf'
            self.suggested_results     = fname[:-4] + '-notas.xlsx'

            self.ui.labelExamsFileName.setText(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def open_names(self) -> None:
        '''Select spreadsheet file with candidates names'''

        fname = self.get_open_fname(
            'Selecione planilha com a lista dos nomes dos candidatos',
            'xlsx'
        )

        if not fname: return

        self.last_dir = Path(fname).parent

        accept = self.load_names_or_exams(
            partial(
                self.uimodel.set_names,
                fname,
                self.ui.lineEditNameFistName.text()
            ),
            'os nomes'
        )

        if accept:
            self.ui.labelNamesFileName.setText(fname)
            self.update()

#--------------------------------------------------------------------------#
    def set_first_cell(self) -> None:

        if not self.uimodel.has_names: return

        accept = self.load_names_or_exams(
            partial(
                self.uimodel.set_names,
                self.ui.labelNamesFileName  .text(),
                self.ui.lineEditNameFistName.text()
            ),
            'os nomes'
        )

        if accept:
            self.update()

    #--------------------------------------------------------------------------#
    def load_names_or_exams(
        self,
        load_function: Callable[[None], None],
        item: str
    ) -> bool:

        message = ''
        title   = f'Erro lendo {item}'
        accept  = True

        try:
            load_function()

        except (
            IOError,
            FileNotFoundError,
            RuntimeError
        ) as er:
            message = (
                f'Não foi possível ler o arquivo com {item}!\n\n'
                f'Mensagem: {str(er)}'
            )
            accept = False

        except IndexError as er:
            message = str(er)
            title   = f'Inconsistência lendo {item}'

        if message:
            self.error_box(title, message)

        return accept

    #--------------------------------------------------------------------------#
    def remove_names(self) -> None:
        '''Remove the candidates names'''

        self.uimodel.remove_names()

        self.ui.lineEditNameFistName.setText('A2')
        self.ui.labelNamesFileName  .setText('')

        self.update()

    #--------------------------------------------------------------------------#
    def choose_results(self) -> None:
        '''Choose spreadsheet file to save the results'''

        fname = self.get_save_fname(
            'Selecione o arquivo para salvar as notas',
            'xlsx',
            self.suggested_results
        )

        if not fname:
            return

        try:
            self.uimodel.set_results(fname)

        except IOError as er:
            self.error_box(
                'Erro lendo o gabarito',
                f'Não foi possível ler o gabarito!\n\n{str(er)}'
            )

        else:
            self.last_dir = Path(fname).parent
            self.ui.labelOutputResultsFileName.setText(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def choose_annotations(self) -> None:
        '''Choose PDF file to save the results'''

        fname = self.get_save_fname(
            'Arquivo para salvar as anotações',
            'pdf',
            self.suggested_annotations
        )

        if fname:
            self.last_dir = Path(fname).parent
            self.ui.labelOutputAnnotationsFileName.setText(fname)
            self.uimodel.set_annotations(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def open_keys(self) -> None:
        '''Choose TXT file with answer keys'''

        fname = self.get_open_fname(
            'Arquivo com o gabarito',
            'txt'
        )

        if not fname:return

        message = ''

        try:
            keys = self.uimodel.keys_model.read_keys(fname)

        except ValueError as er:
            message = str(er)

        except IOError as er:
            message = f'Não foi possível ler o arquivo!\n\n{str(er)}'

        else:
            self.keys_fname = fname
            self.ui.lineEditKeys.setText(keys)

        if message:
            self.error_box('Erro lendo o gabarito', message)

    #--------------------------------------------------------------------------#
    def save_keys(self) -> None:
        '''Choose TXT file to save answer keys'''

        if not self.keys_fname:
            self.keys_fname = self.get_save_fname(
                'Arquivo para salvar o gabarito',
                'txt'
            )

        if self.keys_fname:
            try:
                self.uimodel.keys_model.write_keys(self.keys_fname)

            except IOError as er:
                self.error_box(
                    'Erro salvando o gabarito',
                    f'Não foi possível salvar o gabarito!\n\n{str(er)}'
                )

    #--------------------------------------------------------------------------#
    def saveas_keys(self) -> None:
        '''Choose new TXT file to save answer keys'''

        fname = self.get_save_fname(
            'Arquivo para salvar o gabarito',
            'txt'
        )

        if fname:
            self.keys_fname = fname
            self.save_keys()

    #--------------------------------------------------------------------------#
    def edit_keys(self) -> None:
        '''Open dialog box to edit answer keys'''

        diag = EditKeysDialog(self.win, self.uimodel.keys_model)

        if diag.exec():
            keys = self.uimodel.keys_model.keys
            self.ui.lineEditKeys.setText(keys)
            self.uimodel.set_keys(keys)

    #--------------------------------------------------------------------------#
    def parse_keys(self) -> None:
        '''Parse line edit keys string to keys model'''

        new_keys = self.ui.lineEditKeys.text()
        self.uimodel.keys_model.set_keys(new_keys)
        self.uimodel.keys_model.update()
        # self.uimodel.set_keys(new_keys)

    #--------------------------------------------------------------------------#
    def set_minimum(self) -> None:
        '''Set the minumum number of correct answers to approval'''

        self.uimodel.set_minimum(self.ui.spinBoxMinimumCorrects.value())

    #--------------------------------------------------------------------------#
    def set_ena_keys(self, year:int) -> None:
        '''Set keys of a predefined ENA year'''

        keys = self.uimodel.keys_model.set_ena_keys(year)
        self.ui.lineEditKeys.setText(keys)

    #--------------------------------------------------------------------------#
    def show(self, get_function: Callable[[None],None]) -> None:
        '''Call default desktop application to show a file'''

        url = QUrl.fromLocalFile(get_function())
        QDesktopServices.openUrl(url)

    #-------------------------------------------------------------------------#
    def show_names(self) -> None:
        '''Show dialog box with first and last candidates names'''

        filename   = self.ui.labelNamesFileName  .text()
        first_name = self.ui.lineEditNameFistName.text()
        names      = self.uimodel.names

        show_names(self.win, filename, first_name, names)

    #-------------------------------------------------------------------------#
    #-------------------------------------------------------------------------#
    def error_box( self, title, message ) -> None:
        '''Convenience function to show error message dialog'''

        QMessageBox.critical(
            self.win,
            title,
            message,
            buttons=QMessageBox.StandardButton.Ok
        )

    #--------------------------------------------------------------------------#
    def get_open_fname(self, title: str, ext: str) -> str:
        '''Convenience function to show file open dialog'''

        fname, _ = QFileDialog.getOpenFileName(
            parent  = self.win,
            caption = title,
            dir     = str(self.last_dir),
            filter  = '*.' + ext
        )
        return fname

    #--------------------------------------------------------------------------#
    def get_save_fname(self, title: str, ext: str, suggestion: str = '') -> str:
        '''Convenience function to show file save dialog'''

        if not suggestion:
            suggestion = self.last_dir

        fname, _ = QFileDialog.getSaveFileName(
            parent  = self.win,
            caption = title,
            dir     = suggestion,
            filter  = '*.' + ext
        )

        if fname:
            ee = '.' + ext
            nn = len(ee)
            if len(fname) < nn or fname[-nn:] != ee:
                fname += ee

        return fname

#------------------------------------------------------------------------------#
