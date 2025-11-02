#------------------------------------------------------------------------------#

from PySide6.QtCore    import QUrl
from PySide6.QtWidgets import QWidget, QMainWindow, QTextBrowser

import ena_param as ep

#------------------------------------------------------------------------------#
class HelpWindow(QMainWindow):
    '''Help window'''

    #--------------------------------------------------------------------------#
    def __init__(self, parent: QWidget) -> None:
        '''Initialize help window instance'''

        super().__init__(parent)

        help_path = ep.RESOURCES / 'help.md'
        help_url  = QUrl.fromLocalFile(str(help_path))

        self.help = QTextBrowser()
        self.help.setAcceptRichText(True)
        self.help.setSource(help_url)

        self.setWindowTitle(ep.TITLE + ' - Ajuda')
        self.setCentralWidget(self.help)
        self.resize(800, 600)

        self.show()

#------------------------------------------------------------------------------#
def show_help(parent: QWidget) -> None:
    '''Show help window'''

    HelpWindow(parent)

#------------------------------------------------------------------------------#
