#------------------------------------------------------------------------------#

import sys
sys.path.append('.')

from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import QApplication

from ui.main_window    import MainWindow
from ui.main_controler import MainControler

import resources_rc

#------------------------------------------------------------------------------#
def main( argv ):

    try:
        from ctypes import windll
        myappid = 'Prof_Luis_A_DAfonseca.Corretor_ENA'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    app = QApplication(argv)
    app.setStyle('fusion')
    app.setWindowIcon(QIcon(':/icons/icon.ico'))
    
    window = MainWindow()
    window.show()

    main_controler = MainControler( window )

    return app.exec()

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    main( sys.argv )

#------------------------------------------------------------------------------#
