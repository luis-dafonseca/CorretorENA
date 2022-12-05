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

        text_file = Path(__file__).resolve().parent.parent / 'resources' / 'documentacao.md'
        text_url  = QUrl.fromLocalFile(str(text_file))

        print(text_file)

        self.text = QTextBrowser()
        self.text.setAcceptRichText   (True)
        self.text.setOpenExternalLinks(True)
        self.text.setSource( text_url )

        self.setWindowTitle( ep.TITLE + ' - Ajuda')
        self.setGeometry(100, 60, 800, 600)
        self.setCentralWidget( self.text )

        self.show()

#------------------------------------------------------------------------------#
