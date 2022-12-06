#------------------------------------------------------------------------------#

from PySide6.QtCore    import QUrl
from PySide6.QtWidgets import QMainWindow, QTextBrowser

import ena_param as ep

#------------------------------------------------------------------------------#
class HelpWindow(QMainWindow):

    #--------------------------------------------------------------------------#
    def __init__( self, parent ):

        super().__init__(parent)

        help_path = ep.RESOURCES / 'help.md'
        help_url  = QUrl.fromLocalFile(str(help_path))

        self.help = QTextBrowser()
        self.help.setAcceptRichText(True)
        self.help.setSource( help_url )

        self.setWindowTitle( ep.TITLE + ' - Ajuda')
        self.setCentralWidget( self.help )
        self.resize( 800, 600 )

        self.show()

#------------------------------------------------------------------------------#
