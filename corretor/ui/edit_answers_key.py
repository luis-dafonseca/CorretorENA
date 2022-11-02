#!/usr/bin/python
#------------------------------------------------------------------------------#

import sys
from PySide6.QtCore    import ( Qt,
                                QRegularExpression )
from PySide6.QtGui     import ( QAction,
                                QFontDatabase,
                                QActionGroup, 
                                QRegularExpressionValidator )
from PySide6.QtWidgets import ( QApplication,
                                QMainWindow, 
                                QPushButton, 
                                QToolButton, 
                                QWidget,     
                                QVBoxLayout, 
                                QHBoxLayout, 
                                QGridLayout, 
                                QLabel,      
                                QRadioButton,
                                QButtonGroup,
                                QLineEdit,   
                                QFrame,   
                                QDialogButtonBox )

#------------------------------------------------------------------------------#
class EditModel:

    #--------------------------------------------------------------------------#
    def __init__(self, keys='A'*30 ):

        self.line_to_key( keys )
        self.mask = '>'+(' '+'A'*5)*6
        self.re   = QRegularExpression((' '+'[ABCDEX]'*5)*6)

    #--------------------------------------------------------------------------#
    def set_key( self, ii, cc ):
        self.keys = self.keys[:ii] + cc + self.keys[ii+1:]

    #--------------------------------------------------------------------------#
    def line_to_key( self, line ):
        self.keys = ''.join(line.split())

#------------------------------------------------------------------------------#
class EditAnswersKey(QMainWindow):

    #--------------------------------------------------------------------------#
    def __init__(self, parent, keys ):

        super().__init__()

        self.model = EditModel( keys )

        self.setWindowTitle('Edição do Gabarito')

        layout = QVBoxLayout()
        layout.addWidget(self.keys_form())
        layout.addWidget(self.keys_edit())
        layout.addWidget(self.button_box())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    #--------------------------------------------------------------------------#
    def keys_semi_form(self, N):

        layout = QGridLayout()

        for ii in range(15):

            label = QLabel(str(ii+N+1), self)
            layout.addWidget( label, ii, 0 )

            group = QActionGroup(self)
            group.triggered.connect(lambda state, x=ii+N: self.set_key(x) )

            for jj, cc in enumerate('ABCDEX'):

                action = QAction(cc,self)
                action.setCheckable(True)
                group.addAction(action)

                if cc == self.model.keys[ii]:
                    action.setChecked(True)

                button = QToolButton(self)
                button.setToolButtonStyle(Qt.ToolButtonTextOnly)
                button.setDefaultAction(action)

                if cc == 'X':
                    button.setStyleSheet('QToolButton:checked {background-color: #FF0000;}')
                else:
                    button.setStyleSheet('QToolButton:checked {background-color: #0000FF;}')

                layout.addWidget( button, ii, jj+1 )

            self.groups[ii+N] = group

        frame = QFrame()
        frame.setFrameStyle( QFrame.StyledPanel | QFrame.Sunken)
        frame.setLayout(layout)

        return frame

    #--------------------------------------------------------------------------#
    def keys_form(self):

        self.groups = [None]*30
 
        layout = QHBoxLayout()
        layout.addWidget( self.keys_semi_form( 0) )
        layout.addWidget( self.keys_semi_form(15) )

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    #--------------------------------------------------------------------------#
    def keys_edit(self):

        layout = QHBoxLayout()

        label = QLabel('Gabarito: ', self)

        self.edit = QLineEdit( self.model.keys, self )
        self.edit.editingFinished.connect(self.parse_line_edit)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.edit.setFont(font)

        self.edit.setInputMask( self.model.mask )
        validator = QRegularExpressionValidator(self.model.re, self)
        self.edit.setValidator(validator)

        layout.addWidget( label )
        layout.addWidget( self.edit )

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    #--------------------------------------------------------------------------#
    def button_box(self):

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        button_box = QDialogButtonBox( buttons, self)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        return button_box

    #--------------------------------------------------------------------------#
    def set_key( self, ii ):

        cc = self.groups[ii].checkedAction().iconText()

        self.model.set_key( ii, cc )

        self.edit.setText( self.model.keys )

    #--------------------------------------------------------------------------#
    def parse_line_edit(self):

        self.model.line_to_key( self.edit.text() )

        for ii, cc in enumerate(self.model.keys):

            jj = 'ABCDEX'.index(cc)

            aa = (self.groups[ii].actions())[jj]

            aa.setChecked(True)

    #--------------------------------------------------------------------------#
    def accept(self):
        self.close()

    #--------------------------------------------------------------------------#
    def reject(self):
        self.close()

#------------------------------------------------------------------------------#
