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

from ui.main_model      import MainModel
from ui.keys_model      import KeysModel
from ui.keys_dialog     import EditKeysDialog
from ui.progress_dialog import ProgressDialog
from ui.show_help       import show_help
from ui.show_names      import show_names
from ui.show_summary    import show_summary

import ui.keys_validator as kval

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

        self.keys_model = KeysModel()
        self.main_model = MainModel()

        self.main_model.set_keys(self.keys_model.get_keys())

        self.start_line_edits()
        self.connectSignalsAndSlots()

    #--------------------------------------------------------------------------#
    # GUI functions
    #--------------------------------------------------------------------------#
    def start_line_edits(self) -> None:
        '''Initialise line edit widgets'''

        self.ui.lineEditKeys.setFont     (kval.FONT)
        self.ui.lineEditKeys.setInputMask(kval.MASK)
        self.ui.lineEditKeys.setValidator(kval.validator(self.win))

        self.ui.lineEditKeys.setText(self.keys_model.get_keys())

        regex     = QRegularExpression         ('[A-Z][1-9]')
        validator = QRegularExpressionValidator(regex, self.win)

        self.ui.lineEditFirstCell.setFont     (kval.FONT)
        self.ui.lineEditFirstCell.setInputMask('>AD')
        self.ui.lineEditFirstCell.setValidator(validator)

    #--------------------------------------------------------------------------#
    def connectSignalsAndSlots(self) -> None:
        '''Initialise callbacks'''

        ui = self.ui

        ui.action_Run  .triggered.connect(self.run)
        ui.pushButtonRun .clicked.connect(self.run)
        ui.pushButtonExit.clicked.connect(self.exit)

        ui.action_Exit .triggered.connect(self.exit)
        ui.action_About.triggered.connect(self.about)
        ui.action_Help .triggered.connect(self.help)

        ui.action_Keys_Open  .triggered.connect(self.open_keys)
        ui.action_Keys_Save  .triggered.connect(self.save_keys)
        ui.action_Keys_Saveas.triggered.connect(self.saveas_keys)

        for yy in self.keys_model.get_ena_years():
            action = QAction(f'ENA {yy}', self.win)
            action.triggered.connect(partial(self.set_ena_keys, yy))
            ui.menuKeys.addAction(action)

        ui.pushButtonKeysEdit  .clicked.connect(self.edit_keys)
        ui.lineEditKeys.editingFinished.connect(self.parse_keys)
        ui.spinBoxMinimum .valueChanged.connect(self.set_minimum)

        ui.pushButtonModelLoad.clicked.connect(self.load_model)
        ui.pushButtonExamsLoad.clicked.connect(self.load_exams)

        ui.pushButtonNamesToggle    .clicked.connect(self.toggle_names)
        ui.pushButtonNamesCheck     .clicked.connect(self.show_names)
        ui.lineEditFirstCell.editingFinished.connect(self.set_first_cell)

        ui.pushButtonOutputResultsChoose    .clicked.connect(self.choose_results)
        ui.pushButtonOutputAnnotationsChoose.clicked.connect(self.choose_annotations)

        def open_connect(widget, function: Callable[[None],None]) -> None:
            widget.clicked.connect(partial(self.open, function))

        model = self.main_model

        open_connect(ui.pushButtonModelOpen,       model.get_model_pdf      )
        open_connect(ui.pushButtonKeysOpen,        model.get_keys_pdf       )
        open_connect(ui.pushButtonExamsOpen,       model.get_exams_pdf      )
        open_connect(ui.pushButtonNamesOpen,       model.get_names_xlsx     )
        open_connect(ui.pushButtonResultsOpen,     model.get_results_xlsx   )
        open_connect(ui.pushButtonAnnotationsOpen, model.get_annotations_pdf)

    #--------------------------------------------------------------------------#
    def update(self) -> None:
        '''Update window widgets'''

        has_model   = self.main_model.has_model
        has_exams   = self.main_model.has_exams
        has_names   = self.main_model.has_names
        has_results = self.main_model.has_results
        has_annot   = self.main_model.has_annot

        self.ui.pushButtonModelOpen.setEnabled(has_model)
        self.ui.pushButtonKeysOpen .setEnabled(has_model)
        self.ui.labelModelFileName .setEnabled(has_model)

        self.ui.pushButtonExamsOpen.setEnabled(has_exams)
        self.ui.labelExamsFileName .setEnabled(has_exams)

        self.ui.pushButtonNamesOpen .setEnabled(has_names)
        self.ui.pushButtonNamesCheck.setEnabled(has_names)
        self.ui.labelNamesFileName  .setEnabled(has_names)

        self.ui.labelOutputResultsFileName    .setEnabled(has_results)
        self.ui.labelOutputAnnotationsFileName.setEnabled(has_annot)

        done = self.main_model.done

        self.ui.pushButtonResultsOpen    .setEnabled(done)
        self.ui.pushButtonAnnotationsOpen.setEnabled(done)

        ready = self.main_model.ready_to_run() and not done
        self.ui.action_Run   .setEnabled(ready)
        self.ui.pushButtonRun.setEnabled(ready)

        num_exams = self.main_model.num_exams
        num_names = self.main_model.num_names

        if done:
            total = self.main_model.summary['total']
            message = f'{total} provas corrigidas'

        elif self.main_model.has_conflict():
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
    def about(self) -> None:
        '''Show about dialog box'''

        title   = ep.TITLE + ' - Sobre'
        message = ep.ABOUT + '\n' + ' '*120

        QMessageBox.about(self.win, title, message)

    #--------------------------------------------------------------------------#
    def help(self) -> None:
        '''Show help window'''

        show_help(self.win)

    #--------------------------------------------------------------------------#
    # Execution function
    #--------------------------------------------------------------------------#
    def run(self) -> None:
        '''Execute the correction'''

        if self.main_model.has_conflict():
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

        progress = ProgressDialog(self.win, f'{ep.TITLE} - Correção')

        try:
            finished = self.main_model.run(progress)

        except IOError as er:
            self.error_box(
                'Erro salvando os arquivos',
                ('Não foi possível salvar algum dos arquivos!'
                 f'\n\n{str(er)}'
                )
            )

        else:
            show_summary(self.win, finished, self.main_model.summary)

        self.update()

    #--------------------------------------------------------------------------#
    # Exams model and answers functions
    #--------------------------------------------------------------------------#
    def load_model(self) -> None:
        '''Open PDF file with model'''

        fname = self.get_open_fname(
            'Selecione o modelo da folha de respostas',
            'pdf'
        )

        if not fname: return

        self.last_dir = Path(fname).parent

        message = ''

        try:
            self.main_model.set_model(fname)

        except ValueError as er:
            message = str(er)

        except (
            IOError,
            FileNotFoundError,
            RuntimeError
        ) as er:
            message = (
                f'Não foi possível ler o arquivo com o modelo!\n\n'
                f'{str(er)}'
            )

        else:
            self.ui.labelModelFileName.setText(fname)
            self.update()

        if message:
            self.error_box('Erro lendo o modelo', message)

    #--------------------------------------------------------------------------#
    def load_exams(self) -> None:
        '''Open PDF file with exams'''

        fname = self.get_open_fname(
            'Selecione o arquivo com as respostas para serem corrigidas',
            'pdf'
        )

        if not fname: return

        self.last_dir = Path(fname).parent

        accept = self.load_names_or_exams(
            partial(self.main_model.set_exams, fname),
            'as respostas'
            )

        if accept:
            self.suggested_annotations = fname[:-4] + '-anotacoes.pdf'
            self.suggested_results     = fname[:-4] + '-notas.xlsx'

            self.ui.labelExamsFileName.setText(fname)
            self.update()

    #--------------------------------------------------------------------------#
    # List of names functions
    #--------------------------------------------------------------------------#
    def toggle_names(self) -> None:
        '''Load or remove the candidates names'''

        if self.main_model.has_names:
            self.remove_names()
        else:
            self.load_names()

    #--------------------------------------------------------------------------#
    def remove_names(self) -> None:
        '''Remove the candidates names'''

        self.main_model.remove_names()

        self.ui.pushButtonNamesToggle.setText('Carregar')
        self.ui.lineEditFirstCell    .setText('A2')
        self.ui.labelNamesFileName   .setText('')

        self.update()

    #--------------------------------------------------------------------------#
    def load_names(self) -> None:
        '''Select spreadsheet file with candidates names'''

        fname = self.get_open_fname(
            'Selecione planilha com a lista dos nomes dos candidatos',
            'xlsx'
        )

        if not fname: return

        self.last_dir = Path(fname).parent

        accept = self.load_names_or_exams(
            partial(
                self.main_model.set_names,
                fname,
                self.ui.lineEditFirstCell.text()
            ),
            'os nomes'
        )

        if accept:
            self.ui.pushButtonNamesToggle.setText('Remover')
            self.ui.labelNamesFileName.setText(fname)
            self.update()

#--------------------------------------------------------------------------#
    def set_first_cell(self) -> None:

        if not self.main_model.has_names: return

        accept = self.load_names_or_exams(
            partial(
                self.main_model.set_names,
                self.ui.labelNamesFileName.text(),
                self.ui.lineEditFirstCell .text()
            ),
            'os nomes'
        )

        if accept:
            self.update()

    #--------------------------------------------------------------------------#
    def load_names_or_exams(
        self,
        model_set_function: Callable[[None], None],
        item: str
    ) -> bool:

        message = ''
        title   = f'Erro lendo {item}'
        accept  = True

        try:
            model_set_function()

        except (
            IOError,
            FileNotFoundError,
            RuntimeError
        ) as er:
            message = (str(er))
            accept  = False

        except IndexError as er:
            message = str(er)
            title   = f'Inconsistência lendo {item}'

        if message:
            self.error_box(title, message)

        return accept

    #--------------------------------------------------------------------------#
    # Results and Annotations functions
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
            self.main_model.set_results(fname)

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
            self.main_model.set_annotations(fname)
            self.update()

    #--------------------------------------------------------------------------#
    # Keys and minimum score functions
    #--------------------------------------------------------------------------#
    def open_keys(self) -> None:
        '''Choose TXT file with answer keys'''

        fname = self.get_open_fname('Arquivo com o gabarito', 'txt')

        if not fname: return

        message = ''

        try:
            keys = self.keys_model.read_keys(fname)

        except ValueError as er:
            message = str(er)

        except IOError as er:
            message = f'Não foi possível ler o arquivo!\n\n{str(er)}'

        else:
            self.ui.lineEditKeys.setText(keys)

        if message:
            self.error_box('Erro lendo o gabarito', message)
        else:
            self.main_model.set_keys(self.keys_model.get_keys())
            self.update()

    #--------------------------------------------------------------------------#
    def save_keys(self) -> None:
        '''Choose TXT file to save answer keys'''

        if not self.keys_model.fname:
            self.keys_model.fname = self.get_save_fname(
                'Arquivo para salvar o gabarito',
                'txt'
            )

        if self.keys_model.fname:
            try:
                self.keys_model.write_keys()

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
            self.keys_model.fname = fname
            self.save_keys()

    #--------------------------------------------------------------------------#
    def edit_keys(self) -> None:
        '''Open dialog box to edit answer keys'''

        diag = EditKeysDialog(self.win, self.keys_model)

        if diag.exec():
            keys = self.keys_model.get_keys()
            self.ui.lineEditKeys.setText(keys)
            self.main_model.set_keys(keys)
            self.update()

    #--------------------------------------------------------------------------#
    def parse_keys(self) -> None:
        '''Parse line edit keys string to keys model'''

        new_keys = self.ui.lineEditKeys.text()
        self.keys_model.set_keys(new_keys)
        self.main_model.set_keys(new_keys)
        self.update()

    #--------------------------------------------------------------------------#
    def set_ena_keys(self, year:int) -> None:
        '''Set keys of a predefined ENA year'''

        keys = self.keys_model.set_ena_keys(year)
        self.ui.lineEditKeys.setText(keys)
        self.main_model.set_keys(keys)
        self.update()

    #--------------------------------------------------------------------------#
    def set_minimum(self) -> None:
        '''Set the minimum number of correct answers to approval'''

        self.main_model.set_minimum(self.ui.spinBoxMinimumCorrects.value())
        self.update()

    #--------------------------------------------------------------------------#
    # Show functions
    #--------------------------------------------------------------------------#
    def open(self, get_function: Callable[[None],None]) -> None:
        '''Call default desktop application to show a file'''

        url = QUrl.fromLocalFile(get_function())
        QDesktopServices.openUrl(url)

    #-------------------------------------------------------------------------#
    def show_names(self) -> None:
        '''Show dialog box with first and last candidates names'''

        filename   = self.ui.labelNamesFileName.text()
        first_name = self.ui.lineEditFirstCell .text()
        names      = self.main_model.names

        show_names(self.win, filename, first_name, names)

    #-------------------------------------------------------------------------#
    # Convenience functions
    #-------------------------------------------------------------------------#
    def error_box( self, title, message ) -> None:
        '''Convenience function to show error message dialog'''

        message = message + '\n' + ' '*90

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
            suggestion = str(self.last_dir)

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
