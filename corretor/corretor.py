#------------------------------------------------------------------------------#

import sys
sys.path.append('.')

from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import QApplication

import ena_param as ep

from ui.main_window    import MainWindow
from ui.main_controler import MainControler

import resources_rc

#------------------------------------------------------------------------------#
def main( argv ):

    try:
        from ctypes import windll
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(ep.MYAPPID)
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
