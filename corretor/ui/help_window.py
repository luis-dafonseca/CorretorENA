#------------------------------------------------------------------------------#

from pathlib           import Path
from PySide6.QtCore    import QUrl
from PySide6.QtWidgets import QMainWindow, QTextEdit

import ena_param as ep

#------------------------------------------------------------------------------#
class HelpWindow(QMainWindow):

    #--------------------------------------------------------------------------#
    def __init__( self, parent ):

        super().__init__(parent)

        text_file = ep.RESOURCES / 'help.md'

        self.text = QTextEdit()
        self.text.setAcceptRichText(True)
        self.text.setReadOnly      (True)
        self.text.setMarkdown( text_file.read_text() )

        self.setWindowTitle( ep.TITLE + ' - Ajuda')
        self.setCentralWidget( self.text )
        self.resize( 800, 600 )

        self.show()

#------------------------------------------------------------------------------#
