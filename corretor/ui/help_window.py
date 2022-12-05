#------------------------------------------------------------------------------#

import os

from PySide6.QtWidgets import QMainWindow, QTextBrowser

import ena_param as ep

#------------------------------------------------------------------------------#
class HelpWindow(QMainWindow):

    #--------------------------------------------------------------------------#
    def __init__( self, parent ):

        super().__init__(parent)

        basedir = os.path.dirname(__file__)

        self.text = QTextBrowser()
        self.text.setAcceptRichText   (True)
        self.text.setOpenExternalLinks(True)
        self.text.setSource(basedir + '/../resources/documentacao.md')

        self.setWindowTitle( ep.TITLE + ' - Ajuda')
        self.setGeometry(100, 60, 800, 600)
        self.setCentralWidget( self.text )

        self.show()

#------------------------------------------------------------------------------#
