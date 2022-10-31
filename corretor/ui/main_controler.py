#------------------------------------------------------------------------------#

import os

from PySide6.QtWidgets  import QApplication, QDialog, QFileDialog, QSizePolicy, QMessageBox
from ui.main_uimodel    import MainUIModel
from ui.show_names      import show_names_window

_DEBUG=False
_DEBUG=True

#------------------------------------------------------------------------------#
def _get_open_pdf( parent, title, directoty ):
    fname, ftr = QFileDialog.getOpenFileName( parent=parent, 
                                              caption=title, 
                                              dir=directoty, 
                                              filter='*.pdf' )
    return fname

#------------------------------------------------------------------------------#
def _get_save_pdf( parent, title, directoty ):
    fname, ftr = QFileDialog.getSaveFileName( parent=parent, 
                                              caption=title, 
                                              dir=directoty, 
                                              filter='*.pdf')
    return fname

#------------------------------------------------------------------------------#
def _get_open_xlsx( parent, title, directoty ):
    fname, ftr = QFileDialog.getOpenFileName( parent=parent, 
                                              caption=title, 
                                              dir=directoty, 
                                              filter='*.xlsx' )
    return fname

#------------------------------------------------------------------------------#
def _get_save_xlsx( parent, title, directoty ):
    fname, ftr = QFileDialog.getSaveFileName( parent=parent, 
                                              caption=title, 
                                              dir=directoty, 
                                              filter='*.xlsx')
    return fname

#------------------------------------------------------------------------------#
def _add_file_extension( fname, ext ):

    ext = '.' + ext
    nn  = len(ext)

    if len(fname) < nn:
        fname += ext
    elif fname[-nn:] != ext:
        fname += ext

    return fname

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self._win = window
        self._ui  = window.ui

        self.last_dir              = '.'
        self.suggested_annotations = ''
        self.suggested_grades      = ''

        self._uimodel = MainUIModel( self._ui.progressBar )

        self._start()
        self._connectSignalsAndSlots()

    #--------------------------------------------------------------------------#
    def _start(self):

        self._ui.labelModelFileName            .setText('')
        self._ui.labelAnswersFileName          .setText('')
        self._ui.labelNamesFileName            .setText('')
        self._ui.labelOutputGradesFileName     .setText('')
        self._ui.labelOutputAnnotationsFileName.setText('')

        size_policy = self._ui.progressBar.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self._ui.progressBar.setSizePolicy( size_policy )
        self._ui.progressBar.hide()

        # DEBUG
        #----------------------------------------------------------------------#
        if _DEBUG:

            fname = './modelo.pdf'
            self._ui.labelModelFileName.setText( fname )
            self._uimodel.set_model( fname )

            fname = './exemplo.pdf'
            self._ui.labelAnswersFileName.setText( fname )
            self._uimodel.set_answers( fname  )

            fname = './exemplo.xlsx'
            first_name = 'A2'
            self._ui.labelNamesFileName.setText( fname )
            self._uimodel.set_names( fname, first_name )

            fname = './exemplo-notas.xlsx'
            self._ui.labelOutputGradesFileName.setText( fname )
            self._uimodel.set_grades( fname )

            fname = './exemplo-anotacoes.pdf'
            self._ui.labelOutputAnnotationsFileName.setText(fname)
            self._uimodel.set_annotations( fname )

            keys = 'C B E A C B E D C B E E A D C C D B A D A D A C D E A E B D'
            self._ui.lineEditKeys.setText( keys )
            self._uimodel.set_keys( keys )

            self._update()

    #--------------------------------------------------------------------------#
    def _connectSignalsAndSlots(self):

        self._ui.action_Run   .triggered.connect( self._run )
        self._ui.pushButtonRun.clicked  .connect( self._run )

        self._ui.action_Exit   .triggered.connect( self._exit )
        self._ui.pushButtonExit.clicked  .connect( self._exit )

        self._ui.action_About.triggered.connect( self._about )
        self._ui.action_Help .triggered.connect( self._help  )

        self._ui.pushButtonModelOpen.clicked.connect( self._model_open )
        self._ui.pushButtonModelShow.clicked.connect( self._model_show )

        self._ui.pushButtonKeysEdit.clicked.connect( self._keys_edit )
        self._ui.pushButtonKeysShow.clicked.connect( self._keys_show )

        self._ui.pushButtonAnswersOpen.clicked.connect( self._answers_open )
        self._ui.pushButtonAnswersShow.clicked.connect( self._answers_show )

        self._ui.pushButtonNamesOpen.clicked.connect( self._names_open )
        self._ui.pushButtonNamesShow.clicked.connect( self._names_show )

        self._ui.pushButtonOutputGradesChoose     .clicked.connect( self._choose_grades      )
        self._ui.pushButtonOutputAnnotationsChoose.clicked.connect( self._choose_annotations )

    #--------------------------------------------------------------------------#
    def _update(self):

        if self._uimodel.has_model:
            self._ui.pushButtonModelShow.setEnabled(True)
            self._ui.labelModelFileName.setEnabled(True)

        if self._uimodel.has_keys:
            self._ui.pushButtonKeysShow.setEnabled(True)

        if self._uimodel.has_answers:
            self._ui.pushButtonAnswersShow.setEnabled(True)
            self._ui.labelAnswersFileName.setEnabled(True)

        if self._uimodel.has_names:
            self._ui.pushButtonNamesShow.setEnabled(True)
            self._ui.labelNamesFileName.setEnabled(True)

        if self._uimodel.has_grades:
            self._ui.labelOutputGradesFileName.setEnabled(True)

        if self._uimodel.has_annotations:
            self._ui.labelOutputAnnotationsFileName.setEnabled(True)

        if self._uimodel.ready_to_run():
            self._ui.action_Run   .setEnabled(True)
            self._ui.pushButtonRun.setEnabled(True)

    #--------------------------------------------------------------------------#
    def _exit(self):
        QApplication.quit()

    #--------------------------------------------------------------------------#
    def _run(self):
        
        self._ui.progressBar.show()
        self._uimodel.run()
        self._ui.progressBar.hide()

        msg = QMessageBox(self._win)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Corretor ENA: Correção Concluída                         ")
        msg.setWindowTitle("Corretor ENA - Conclusão")
        msg.show()

    #--------------------------------------------------------------------------#
    def _about(self):
        print('<about> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _help(self):
        print('<help> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _model_open(self):

        fname = _get_open_pdf( self._win, 
                               'Selecione o modelo da folha de respostas',
                               self.last_dir )

        if fname:
            self.last_dir = os.path.dirname(fname)
            self._ui.labelModelFileName.setText( fname )
            self._uimodel.set_model( fname )
            self._update()

    #--------------------------------------------------------------------------#
    def _answers_open(self):

        fname = _get_open_pdf( self._win, 
                               'Selecione as respostas para serem corrigidas' ,
                               self.last_dir )

        if fname:

            self.last_dir = os.path.dirname(fname)
            self.suggested_annotations = fname[:-4] + '-anotacoes.pdf'
            self.suggested_grades      = fname[:-4] + '-notas.xlsx'

            self._ui.labelAnswersFileName.setText( fname )
            self._uimodel.set_answers( fname  )
            self._update()

    #--------------------------------------------------------------------------#
    def _names_open(self):

        fname = _get_open_xlsx( self._win, 
                                'Selecione a lista dos nomes dos candidatos' ,
                                self.last_dir )

        if fname:
            
            first_name = self._ui.lineEditNameFistName.text()

            self.last_dir = os.path.dirname(fname)
            self._ui.labelNamesFileName.setText( fname )
            self._uimodel.set_names( fname, first_name )
            self._update()

    #--------------------------------------------------------------------------#
    def _choose_grades(self):

        fname = _get_save_xlsx( self._win, 
                                'Arquivo para salvar as notas' ,
                                self.suggested_grades )

        if fname:
            fname = _add_file_extension( fname, 'xlsx' )
            self.last_dir = os.path.dirname(fname)
            self._ui.labelOutputGradesFileName.setText( fname )
            self._uimodel.set_grades( fname )
            self._update()

    #--------------------------------------------------------------------------#
    def _choose_annotations(self):

        fname = _get_save_pdf( self._win, 
                               'Arquivo para salvar as anotações' ,
                               self.suggested_annotations )

        if fname:
            fname = _add_file_extension( fname, 'pdf' )
            self.last_dir = os.path.dirname(fname)
            self._ui.labelOutputAnnotationsFileName.setText(fname)
            self._uimodel.set_annotations( fname )
            self._update()

    #--------------------------------------------------------------------------#
    def _keys_edit(self):

        keys = 'C B E A C B E D C B E E A D C C D B A D A D A C D E A E B D'

        self._ui.lineEditKeys.setText( keys )
        self._uimodel.set_keys( keys )

    #--------------------------------------------------------------------------#
    def _model_show(self):
        print('<model_show> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _keys_show(self):
        print('<_keys_show> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _answers_show(self):
        print('<_answers_show> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _names_show(self):

        filename   = self._ui.labelNamesFileName  .text()
        first_name = self._ui.lineEditNameFistName.text()
        names      = self._uimodel.names

        show_names_window( self._win, filename, first_name, names )

#------------------------------------------------------------------------------#
