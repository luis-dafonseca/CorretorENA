#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication, QMainWindow
from ui.form_show_pdf  import Ui_ShowPDF

#------------------------------------------------------------------------------#
def show_pdf_window( parent, title, qimag ):

    window = QMainWindow(parent)
    window.ui = Ui_ShowPDF()
    window.ui.setupUi(window)
    
    screen = QApplication.primaryScreen()
    h = int( 0.8 * screen.size().height() )

    qimag = qimag.scaledToHeight(h)

    window.setWindowTitle(title)
    window.ui.labelPDFImage.setPixmap(qimag)

    window.show()

#------------------------------------------------------------------------------#
