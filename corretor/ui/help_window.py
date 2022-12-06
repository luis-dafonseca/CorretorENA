#------------------------------------------------------------------------------#

from pathlib           import Path
from PySide6.QtCore    import QUrl
from PySide6.QtWidgets import QMainWindow, QTextBrowser

import ena_param as ep

#------------------------------------------------------------------------------#
class HelpWindow(QMainWindow):

    #--------------------------------------------------------------------------#
    def __init__( self, parent ):

        super().__init__(parent)

        text_file = ep.RESOURCES / 'documentacao.md'
        text_url  = QUrl.fromLocalFile(str(text_file))

        self.text = QTextBrowser()
        self.text.setAcceptRichText   (True)
        self.text.setOpenExternalLinks(True)
        self.text.setSource( text_url )

        self.setWindowTitle( ep.TITLE + ' - Ajuda')
        self.setCentralWidget( self.text )
        self.resize( 800, 600 )

        self.show()

#------------------------------------------------------------------------------#
