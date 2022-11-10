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

from ui.main_uimodel     import MainUIModel
from ui.show_names       import show_names_window
from ui.edit_keys_dialog import EditKeysDialog

#------------------------------------------------------------------------------#
def _get_open_fname( parent_, title_, directoty_, ext_ ):
    fname, _ = QFileDialog.getOpenFileName( parent  = parent_, 
                                            caption = title_, 
                                            dir     = directoty_, 
                                            filter  = '*.' + ext_ )
    return fname

#------------------------------------------------------------------------------#
def _get_save_fname( parent_, title_, directoty_, ext_ ):
    fname, _ = QFileDialog.getSaveFileName( parent  = parent_, 
                                            caption = title_, 
                                            dir     = directoty_, 
                                            filter  = '*.' + ext_ )
    if fname:
        ee = '.' + ext_
        nn = len(ee)
        if len(fname) < nn or fname[-nn:] != ee:
            fname += ee

    return fname

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self._win = window
        self._ui  = window.ui

        self._last_dir              = '.'
        self._suggested_annotations = ''
        self._suggested_grades      = ''
        self._keys_fname            = ''

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

        k_model = self._uimodel.keys_model

        self._ui.lineEditKeys.setFont     ( k_model.font )
        self._ui.lineEditKeys.setInputMask( k_model.mask )
        self._ui.lineEditKeys.setValidator( k_model.validator(self._win) )
        self._ui.lineEditKeys.setText     ( k_model.keys )

        regex     = QRegularExpression('[A-Z][1-9]')
        validator = QRegularExpressionValidator( regex, self._win )
        self._ui.lineEditNameFistName.setFont     ( k_model.font )
        self._ui.lineEditNameFistName.setInputMask( '>AD' )
        self._ui.lineEditNameFistName.setValidator( validator )

    #--------------------------------------------------------------------------#
    def _connectSignalsAndSlots(self):

        self._ui.action_Run   .triggered.connect( self._run )
        self._ui.pushButtonRun.clicked  .connect( self._run )

        self._ui.action_Exit   .triggered.connect( self._exit )
        self._ui.pushButtonExit.clicked  .connect( self._exit )

        self._ui.action_Keys_Open  .triggered.connect( self._keys_open   )
        self._ui.action_Keys_Save  .triggered.connect( self._keys_save   )
        self._ui.action_Keys_Saveas.triggered.connect( self._keys_saveas )

        self._ui.action_About.triggered.connect( self._about )
        self._ui.action_Help .triggered.connect( self._help  )

        for yy in self._uimodel.keys_model.get_ena_years():
            action = QAction( f'ENA {yy}', self._win )
            action.triggered.connect( partial( self._set_ena_keys, yy ) )
            self._ui.menuKeys.addAction( action )

        self._ui.pushButtonModelOpen.clicked.connect( self._model_open )
        self._ui.pushButtonModelShow.clicked.connect( self._model_show )

        self._ui.pushButtonKeysEdit.clicked  .connect( self._keys_edit )
        self._ui.pushButtonKeysShow.clicked  .connect( self._keys_show )
        self._ui.lineEditKeys.editingFinished.connect( self._parse_keys_edit)

        self._ui.pushButtonAnswersOpen.clicked.connect( self._answers_open )
        self._ui.pushButtonAnswersShow.clicked.connect( self._answers_show )

        self._ui.pushButtonNamesOpen  .clicked.connect( self._names_open   )
        self._ui.pushButtonNamesShow  .clicked.connect( self._names_show   )
        self._ui.pushButtonNamesRemove.clicked.connect( self._names_remove )
        self._ui.lineEditNameFistName.editingFinished.connect( self._set_fisrt_name )

        self._ui.pushButtonOutputGradesChoose     .clicked.connect( self._choose_grades      )
        self._ui.pushButtonOutputAnnotationsChoose.clicked.connect( self._choose_annotations )

    #--------------------------------------------------------------------------#
    def _update(self):

        self._ui.pushButtonModelShow.setEnabled(self._uimodel.has_model)
        self._ui.labelModelFileName .setEnabled(self._uimodel.has_model)
        self._ui.pushButtonKeysShow .setEnabled(self._uimodel.has_model)

        self._ui.pushButtonAnswersShow.setEnabled(self._uimodel.has_answers)
        self._ui.labelAnswersFileName .setEnabled(self._uimodel.has_answers)

        self._ui.pushButtonNamesShow  .setEnabled(self._uimodel.has_names)
        self._ui.pushButtonNamesRemove.setEnabled(self._uimodel.has_names)
        self._ui.labelNamesFileName   .setEnabled(self._uimodel.has_names)

        self._ui.labelOutputGradesFileName     .setEnabled(self._uimodel.has_grades)
        self._ui.labelOutputAnnotationsFileName.setEnabled(self._uimodel.has_annotations)

        ready = self._uimodel.ready_to_run()
        self._ui.action_Run   .setEnabled(ready)
        self._ui.pushButtonRun.setEnabled(ready)

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
        msg.setText('Corretor ENA: Correção Concluída' + ' '*25)
        msg.setWindowTitle('Corretor ENA - Conclusão')
        msg.show()

    #--------------------------------------------------------------------------#
    def _about(self):
        print('<about> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _help(self):
        print('<help> not yet implemented!')

    #--------------------------------------------------------------------------#
    def _model_open(self):

        fname = _get_open_fname( self._win, 'Selecione o modelo da folha de respostas',
                                 self._last_dir, 'pdf' )

        if fname:
            self._last_dir = os.path.dirname(fname)

            try:
                self._uimodel.set_model( fname )

            except ValueError:

                fname = os.path.basename( fname )
                QMessageBox.critical( self._win,
                                      'Erro lendo o modelo', 
                                      f'O arquivo {fname} não contém um modelo!',
                                      buttons=QMessageBox.StandardButton.Ok )

            else:
                self._ui.labelModelFileName.setText( fname )
                self._update()

    #--------------------------------------------------------------------------#
    def _answers_open(self):

        fname = _get_open_fname( self._win, 'Selecione as respostas para serem corrigidas',
                                 self._last_dir, 'pdf' )

        if fname:

            self._last_dir = os.path.dirname(fname)
            self._suggested_annotations = fname[:-4] + '-anotacoes.pdf'
            self._suggested_grades      = fname[:-4] + '-notas.xlsx'

            self._ui.labelAnswersFileName.setText( fname )
            self._uimodel.set_answers( fname  )
            self._update()

    #--------------------------------------------------------------------------#
    def _names_open(self):

        fname = _get_open_fname( self._win, 'Selecione a lista dos nomes dos candidatos',
                                 self._last_dir, 'xlsx' )

        if fname:
            first_name = self._ui.lineEditNameFistName.text()

            self._last_dir = os.path.dirname(fname)
            self._ui.labelNamesFileName.setText( fname )
            self._uimodel.set_names( fname, first_name )
            self._update()

#--------------------------------------------------------------------------#
    def _names_remove(self):
        self._ui.lineEditNameFistName.setText('A2')
        self._ui.labelNamesFileName  .setText( '' )
        self._uimodel.remove_names()
        self._update()

#--------------------------------------------------------------------------#
    def _set_fisrt_name(self):
        if self._uimodel.has_names:
            fname      = self._ui.labelNamesFileName  .text()
            first_name = self._ui.lineEditNameFistName.text()
            self._uimodel.set_names( fname, first_name )
            self._update()

    #--------------------------------------------------------------------------#
    def _choose_grades(self):

        fname = _get_save_fname( self._win, 'Arquivo para salvar as notas',
                                 self._suggested_grades, 'xlsx' )

        if fname:
            self._last_dir = os.path.dirname(fname)
            self._ui.labelOutputGradesFileName.setText( fname )
            self._uimodel.set_grades( fname )
            self._update()

    #--------------------------------------------------------------------------#
    def _choose_annotations(self):

        fname = _get_save_fname( self._win, 'Arquivo para salvar as anotações',
                                 self._suggested_annotations, 'pdf' )

        if fname:
            self._last_dir = os.path.dirname(fname)
            self._ui.labelOutputAnnotationsFileName.setText(fname)
            self._uimodel.set_annotations( fname )
            self._update()

    #--------------------------------------------------------------------------#
    def _keys_open(self):

        new_keys_fname = _get_open_fname( self._win, 'Arquivo com o gabarito',
                                          self._last_dir, 'txt' )

        if new_keys_fname:

            try:
                keys = self._uimodel.keys_model.read_keys( new_keys_fname )

            except ValueError:

                fname = os.path.basename( new_keys_fname )
                QMessageBox.critical( self._win,
                                      'Erro lendo o gabarito', 
                                      f'O arquivo {fname} não contém um gabarito!',
                                      buttons=QMessageBox.StandardButton.Ok )

            else:
                self._keys_fname = new_keys_fname
                self._ui.lineEditKeys.setText( keys )

    #--------------------------------------------------------------------------#
    def _keys_save(self):

        if not self._keys_fname:
            self._keys_fname = _get_save_fname( self._win, 'Arquivo para salvar o gabarito',
                                                self._last_dir, 'txt' )

        if self._keys_fname:
            with open( self._keys_fname, 'w' ) as f:
                f.write( self._ui.lineEditKeys.text() )

    #--------------------------------------------------------------------------#
    def _keys_saveas(self):

        new_keys_fname = _get_save_fname( self._win, 'Arquivo para salvar o gabarito',
                                          self._last_dir, 'txt' )

        if new_keys_fname:
            self._keys_fname = new_keys_fname
            with open( self._keys_fname, 'w' ) as f:
                f.write( self._ui.lineEditKeys.text() )

    #--------------------------------------------------------------------------#
    def _keys_edit(self):

        diag = EditKeysDialog( self._win, self._uimodel.keys_model )

        if diag.exec():
            keys = self._uimodel.keys_model.keys
            self._ui.lineEditKeys.setText( keys )

    #--------------------------------------------------------------------------#
    def _parse_keys_edit(self):
        self._uimodel.keys_model.set_keys( self._ui.lineEditKeys.text() )
        self._uimodel.keys_model.update()

    #--------------------------------------------------------------------------#
    def _set_ena_keys( self, yy ):
        keys = self._uimodel.keys_model.set_ena_keys(yy)
        self._ui.lineEditKeys.setText( keys )

    #--------------------------------------------------------------------------#
    def _model_show(self):
        QDesktopServices.openUrl( QUrl(f'file:///{self._uimodel.get_model_pdf()}') )

    #--------------------------------------------------------------------------#
    def _keys_show(self):
        QDesktopServices.openUrl( QUrl(f'file:///{self._uimodel.get_keys_pdf()}') )

    #--------------------------------------------------------------------------#
    def _answers_show(self):
        QDesktopServices.openUrl( QUrl(f'file:///{self._uimodel.get_answers_pdf()}') )

    #-------------------------------------------------------------------------#
    def _names_show(self):

        filename   = self._ui.labelNamesFileName  .text()
        first_name = self._ui.lineEditNameFistName.text()
        names      = self._uimodel.names

        show_names_window( self._win, filename, first_name, names )

#------------------------------------------------------------------------------#
