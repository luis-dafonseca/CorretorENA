#------------------------------------------------------------------------------#

import os

from functools         import partial
from PySide6.QtCore    import QRegularExpression, QUrl
from PySide6.QtWidgets import ( QApplication, 
                                QFileDialog, 
                                QMessageBox )
from PySide6.QtGui     import ( QRegularExpressionValidator, 
                                QAction,
                                QDesktopServices )

import ena_param as ep

from ui.main_uimodel     import MainUIModel
from ui.edit_keys_dialog import EditKeysDialog
from ui.progress_dialog  import ProgressDialog
from ui.help_window      import HelpWindow
from ui.show_names       import show_names

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.win = window
        self.ui  = window.ui

        self.last_dir              = str(ep.HOME)
        self.suggested_annotations = ''
        self.suggested_grades      = ''
        self.keys_fname            = ''

        self.uimodel = MainUIModel()

        self.start()
        self.connectSignalsAndSlots()

    #--------------------------------------------------------------------------#
    def start(self):

        k_model = self.uimodel.keys_model

        self.ui.lineEditKeys.setFont     ( k_model.font )
        self.ui.lineEditKeys.setInputMask( k_model.mask )
        self.ui.lineEditKeys.setValidator( k_model.validator(self.win) )
        self.ui.lineEditKeys.setText     ( k_model.keys )

        regex     = QRegularExpression           ('[A-Z][1-9]')
        validator = QRegularExpressionValidator  ( regex, self.win )
        self.ui.lineEditNameFistName.setFont     ( k_model.font )
        self.ui.lineEditNameFistName.setInputMask( '>AD' )
        self.ui.lineEditNameFistName.setValidator( validator )

    #--------------------------------------------------------------------------#
    def connectSignalsAndSlots(self):

        self.ui.action_Run   .triggered.connect( self.run )
        self.ui.pushButtonRun.clicked  .connect( self.run )

        self.ui.action_Exit.triggered.connect( self.exit )

        self.ui.action_Keys_Open  .triggered.connect( self.keys_open   )
        self.ui.action_Keys_Save  .triggered.connect( self.keys_save   )
        self.ui.action_Keys_Saveas.triggered.connect( self.keys_saveas )

        self.ui.action_About.triggered.connect( self.about )
        self.ui.action_Help .triggered.connect( self.help  )

        for yy in self.uimodel.keys_model.get_ena_years():
            action = QAction( f'ENA {yy}', self.win )
            action.triggered.connect( partial( self.set_ena_keys, yy ) )
            self.ui.menuKeys.addAction( action )

        self.ui.pushButtonModelOpen.clicked.connect( self.model_open )
        self.ui.pushButtonModelShow.clicked.connect( self.model_show )

        self.ui.pushButtonKeysEdit.clicked  .connect( self.keys_edit )
        self.ui.pushButtonKeysShow.clicked  .connect( self.keys_show )
        self.ui.lineEditKeys.editingFinished.connect( self.parse_keys_edit)

        self.ui.pushButtonAnswersOpen.clicked.connect( self.answers_open )
        self.ui.pushButtonAnswersShow.clicked.connect( self.answers_show )

        self.ui.pushButtonNamesOpen  .clicked.connect( self.names_open   )
        self.ui.pushButtonNamesShow  .clicked.connect( self.names_show   )
        self.ui.pushButtonNamesRemove.clicked.connect( self.names_remove )
        self.ui.lineEditNameFistName.editingFinished.connect( self.set_fisrt_name )

        self.ui.pushButtonOutputGradesChoose     .clicked.connect( self.choose_grades      )
        self.ui.pushButtonOutputAnnotationsChoose.clicked.connect( self.choose_annotations )

    #--------------------------------------------------------------------------#
    def update(self):

        has_model   = self.uimodel.has_model
        has_answers = self.uimodel.has_answers
        has_names   = self.uimodel.has_names

        self.ui.pushButtonModelShow.setEnabled(has_model)
        self.ui.labelModelFileName .setEnabled(has_model)
        self.ui.pushButtonKeysShow .setEnabled(has_model)

        self.ui.pushButtonAnswersShow.setEnabled(has_answers)
        self.ui.labelAnswersFileName .setEnabled(has_answers)

        self.ui.pushButtonNamesShow  .setEnabled(has_names)
        self.ui.pushButtonNamesRemove.setEnabled(has_names)
        self.ui.labelNamesFileName   .setEnabled(has_names)

        self.ui.labelOutputGradesFileName     .setEnabled(self.uimodel.has_grades)
        self.ui.labelOutputAnnotationsFileName.setEnabled(self.uimodel.has_annotations)

        ready = self.uimodel.ready_to_run()
        self.ui.labelCorrection.setEnabled(ready)
        self.ui.action_Run     .setEnabled(ready)
        self.ui.pushButtonRun  .setEnabled(ready)

        num_answers = self.uimodel.num_answers
        num_names   = self.uimodel.num_names

        if self.uimodel.has_conflict():
            message = f'Aten????o: A quantidade de respostas ({num_answers}) n??o coincide com a quantidade de nomes ({num_names})'

        elif has_answers:
            message = f'Corrigir {num_answers} provas'
        
        else:
            message = 'Corrigir provas'

        self.ui.labelCorrection.setText(message)


    #--------------------------------------------------------------------------#
    def exit(self):
        QApplication.quit()

    #--------------------------------------------------------------------------#
    def run(self):

        if self.uimodel.has_conflict():
            ans = QMessageBox.question( self.win, 'Conflito', 
                                       'A quantidade de respostas n??o coincide com a quantidade de nomes.\n\nCorrigir mesmo assim?' )

            if ans == QMessageBox.No:
                return

        progress = ProgressDialog( self.win, ep.TITLE+' - Corre????o' )

        try:
            finished = self.uimodel.run(progress)

        except IOError as er:
            self.error_box( 'Erro salvando os arquivos', 'N??o foi poss??vel salvar algum arquivo!\n\n{str(er)}' )

        else:
            msg = QMessageBox(self.win)
            msg.setIcon(QMessageBox.Information)

            if finished:
                msg.setWindowTitle( ep.TITLE+' - Conclus??o')
                msg.setText(        ep.TITLE+': Corre????o Conclu??da' + ' '*25)
            else:
                msg.setWindowTitle( ep.TITLE+' - Conclus??o')
                msg.setText(        ep.TITLE+': Corre????o Cancelada' + ' '*25)

            msg.show()

    #--------------------------------------------------------------------------#
    def about(self):
        QMessageBox.about( self.win, ep.TITLE+' - Sobre', ep.ABOUT )

    #--------------------------------------------------------------------------#
    def help(self):
        HelpWindow( self.win )

    #--------------------------------------------------------------------------#
    def model_open(self):

        fname = self.get_open_fname( 'Selecione o modelo da folha de respostas', 'pdf' )

        if not fname:
            return

        self.last_dir = os.path.dirname(fname)

        message = ''

        try:
            self.uimodel.set_model(fname)

        except ValueError as er:
            message = str(er)

        except IOError as er:
            message = f'N??o foi poss??vel ler o arquivo!\n\n{srt(er)}'

        else:
            self.ui.labelModelFileName.setText(fname)
            self.update()

        if message:
            self.error_box( 'Erro lendo o modelo', message )

    #--------------------------------------------------------------------------#
    def answers_open(self):

        fname = self.get_open_fname( 'Selecione as respostas para serem corrigidas', 'pdf' )

        if not fname:
            return

        self.last_dir = os.path.dirname(fname)

        message = ''
        accept  = True

        try:
            self.uimodel.set_answers(fname)

        except ValueError as er:
            message = str(er)
            accept  = False

        except IndexError as er:
            message = str(er)

        except IOError as er:
            message = f'N??o foi poss??vel ler o arquivo!\n\n{srt(er)}'
            accept  = False

        if message:
            self.error_box( 'Erro lendo as respostas', message )

        if accept:
            self.suggested_annotations = fname[:-4] + '-anotacoes.pdf'
            self.suggested_grades      = fname[:-4] + '-notas.xlsx'

            self.ui.labelAnswersFileName.setText(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def names_open(self):

        fname = self.get_open_fname( 'Selecione a lista dos nomes dos candidatos', 'xlsx' )

        if not fname:
            return

        self.last_dir = os.path.dirname(fname)

        message = ''
        accept  = True

        try:
            first_name = self.ui.lineEditNameFistName.text()
            self.uimodel.set_names( fname, first_name )

        except ValueError as er:
            message = str(er)
            accept  = False

        except IndexError as er:
            message = str(er)

        except IOError as er:
            message = f'N??o foi poss??vel ler o arquivo!\n\n{srt(er)}'
            accept  = False

        if message:
            self.error_box( 'Erro lendo os nomes', message )

        if accept:
            self.ui.labelNamesFileName.setText(fname)
            self.update()

#--------------------------------------------------------------------------#
    def names_remove(self):

        self.uimodel.remove_names()

        self.ui.lineEditNameFistName.setText('A2')
        self.ui.labelNamesFileName  .setText( '' )
        
        self.update()

#--------------------------------------------------------------------------#
    def set_fisrt_name(self):

        if not self.uimodel.has_names:
            return
            
        message = ''
        accept  = True
        
        try:
            fname      = self.ui.labelNamesFileName  .text()
            first_name = self.ui.lineEditNameFistName.text()
            self.uimodel.set_names( fname, first_name )

        except ValueError as er:
            message = str(er)
            accept  = False

        except IndexError as er:
            message = str(er)

        except IOError as er:
            message = f'N??o foi poss??vel ler o arquivo!\n\n{srt(er)}'
            accept  = False

        if message:
            self.error_box( 'Erro lendo os nomes', message )

        if accept:
            self.ui.labelNamesFileName.setText(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def choose_grades(self):

        fname = self.get_save_fname( 'Arquivo para salvar as notas', 'xlsx',
                                     self.suggested_grades )

        if not fname:
            return

        try:
            self.uimodel.set_grades(fname)

        except IOError as er:
            self.error_box( 'Erro lendo o gabarito', f'N??o foi poss??vel ler o gabarito!\n\n{srt(er)}' )

        else:
            self.last_dir = os.path.dirname(fname)
            self.ui.labelOutputGradesFileName.setText(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def choose_annotations(self):

        fname = self.get_save_fname( 'Arquivo para salvar as anota????es', 'pdf',
                                     self.suggested_annotations )

        if fname:
            self.last_dir = os.path.dirname(fname)
            self.ui.labelOutputAnnotationsFileName.setText(fname)
            self.uimodel.set_annotations(fname)
            self.update()

    #--------------------------------------------------------------------------#
    def keys_open(self):

        fname = self.get_open_fname( 'Arquivo com o gabarito', 'txt' )

        if not fname:
            return

        message = ''

        try:
            keys = self.uimodel.keys_model.read_keys(fname)

        except ValueError as er:
            message = str(er)

        except IOError as er:
            message = f'N??o foi poss??vel ler o arquivo!\n\n{srt(er)}'

        else:
            self.keys_fname = fname
            self.ui.lineEditKeys.setText(keys)

        if message:
            self.error_box( 'Erro lendo o gabarito', message )

    #--------------------------------------------------------------------------#
    def keys_save(self):

        if not self.keys_fname:
            self.keys_fname = self.get_save_fname( 'Arquivo para salvar o gabarito', 'txt' )

        if self.keys_fname:
            try:
                self.uimodel.keys_model.write_keys( self.keys_fname )

            except IOError as er:
                self.error_box( 'Erro salvando o gabarito', 
                               f'N??o foi poss??vel salvar o gabarito!\n\n{str(er)}' )

    #--------------------------------------------------------------------------#
    def keys_saveas(self):

        fname = self.get_save_fname( 'Arquivo para salvar o gabarito', 'txt' )

        if fname:
            self.keys_fname = fname
            self.keys_save()

    #--------------------------------------------------------------------------#
    def keys_edit(self):

        diag = EditKeysDialog( self.win, self.uimodel.keys_model )

        if diag.exec():
            keys = self.uimodel.keys_model.keys
            self.ui.lineEditKeys.setText( keys )

    #--------------------------------------------------------------------------#
    def parse_keys_edit(self):
        self.uimodel.keys_model.set_keys( self.ui.lineEditKeys.text() )
        self.uimodel.keys_model.update()

    #--------------------------------------------------------------------------#
    def set_ena_keys( self, yy ):
        keys = self.uimodel.keys_model.set_ena_keys(yy)
        self.ui.lineEditKeys.setText( keys )

    #--------------------------------------------------------------------------#
    def model_show(self):
        url = QUrl.fromLocalFile(self.uimodel.get_model_pdf())
        QDesktopServices.openUrl( url )

    #--------------------------------------------------------------------------#
    def keys_show(self):
        url = QUrl.fromLocalFile(self.uimodel.get_keys_pdf())
        QDesktopServices.openUrl( url )

    #--------------------------------------------------------------------------#
    def answers_show(self):
        url = QUrl.fromLocalFile(self.uimodel.get_answers_pdf())
        QDesktopServices.openUrl( url )

    #-------------------------------------------------------------------------#
    def names_show(self):

        filename   = self.ui.labelNamesFileName  .text()
        first_name = self.ui.lineEditNameFistName.text()
        names      = self.uimodel.names

        show_names( self.win, filename, first_name, names )

    #-------------------------------------------------------------------------#
    def error_box( self, title, message ):
        QMessageBox.critical( self.win, title, message,
                              buttons=QMessageBox.StandardButton.Ok )

    #--------------------------------------------------------------------------#
    def get_open_fname( self, title, ext ):
        fname, _ = QFileDialog.getOpenFileName( parent  = self.win, 
                                                caption = title, 
                                                dir     = self.last_dir, 
                                                filter  = '*.' + ext )
        return fname
    
    #--------------------------------------------------------------------------#
    def get_save_fname( self, title, ext, suggestion = '' ):

        if not suggestion:
            suggestion = self.last_dir

        fname, _ = QFileDialog.getSaveFileName( parent  = self.win, 
                                                caption = title, 
                                                dir     = suggestion, 
                                                filter  = '*.' + ext )
        if fname:
            ee = '.' + ext
            nn = len(ee)
            if len(fname) < nn or fname[-nn:] != ee:
                fname += ee
    
        return fname

#------------------------------------------------------------------------------#
