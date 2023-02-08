#------------------------------------------------------------------------------#

from PySide6.QtCore    import Qt
from PySide6.QtGui     import QAction, QActionGroup
from PySide6.QtWidgets import ( QDialog,
                                QToolButton,
                                QVBoxLayout,
                                QHBoxLayout,
                                QGridLayout,
                                QLabel,
                                QLineEdit,
                                QFrame,
                                QDialogButtonBox )

#------------------------------------------------------------------------------#
class EditKeysDialog(QDialog):

    #--------------------------------------------------------------------------#
    def __init__(self, parent, keys_model ):

        super().__init__(parent)

        self.setModal(True)

        self.model = keys_model

        self.setWindowTitle('Edição do Gabarito')

        layout = QVBoxLayout()
        layout.addLayout( self.init_keys_form()  )
        layout.addLayout( self.init_keys_edit()  )
        layout.addWidget( self.init_button_box() )

        self.setLayout(layout)

    #--------------------------------------------------------------------------#
    def init_keys_semi_form(self, N):

        layout = QGridLayout()

        for ii in range(15):

            kk = ii + N

            label = QLabel(str(kk+1), self)
            layout.addWidget( label, ii, 0 )

            group = QActionGroup(self)
            group.triggered.connect(lambda state, x=kk: self.set_key(x) )

            for jj, cc in enumerate('ABCDEX'):

                action = QAction(cc,self)
                action.setCheckable(True)
                group.addAction(action)

                if cc == self.model.keys_next[kk]:
                    action.setChecked(True)

                button = QToolButton(self)
                button.setToolButtonStyle(Qt.ToolButtonTextOnly)
                button.setDefaultAction(action)

                if cc == 'X':
                    button.setStyleSheet('QToolButton:checked {background-color: #FF0000;}')
                else:
                    button.setStyleSheet('QToolButton:checked {background-color: #0000FF;}')

                layout.addWidget( button, ii, jj+1 )

            self.groups[kk] = group

        frame = QFrame()
        frame.setFrameStyle( QFrame.StyledPanel | QFrame.Sunken)
        frame.setLayout(layout)

        return frame

    #--------------------------------------------------------------------------#
    def init_keys_form(self):

        self.groups = [None]*30

        layout = QHBoxLayout()
        layout.addWidget( self.init_keys_semi_form( 0) )
        layout.addWidget( self.init_keys_semi_form(15) )

        return layout

    #--------------------------------------------------------------------------#
    def init_keys_edit(self):

        label = QLabel('Gabarito: ', self)

        self.edit = QLineEdit( self.model.keys_next, self )
        self.edit.textEdited.connect(self.parse_line_edit)

        self.edit.setFont     ( self.model.font )
        self.edit.setInputMask( self.model.mask )
        self.edit.setValidator( self.model.validator(self) )

        layout = QHBoxLayout()
        layout.addWidget( label )
        layout.addWidget( self.edit )

        return layout

    #--------------------------------------------------------------------------#
    def init_button_box(self):

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        button_box = QDialogButtonBox( buttons, self)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        return button_box

    #--------------------------------------------------------------------------#
    def set_key( self, ii ):

        cc = self.groups[ii].checkedAction().iconText()

        self.model.set_key( ii, cc )

        self.edit.setText( self.model.keys_next )

    #--------------------------------------------------------------------------#
    def parse_line_edit(self):

        self.model.set_keys( self.edit.text() )

        for ii, cc in enumerate(self.model.keys_next):

            jj = 'ABCDEX'.index(cc)

            aa = (self.groups[ii].actions())[jj]

            aa.setChecked(True)

    #--------------------------------------------------------------------------#
    def accept(self):
        self.model.update()
        super().accept()

    #--------------------------------------------------------------------------#
    def reject(self):
        self.model.reset()
        super().reject()

#------------------------------------------------------------------------------#
