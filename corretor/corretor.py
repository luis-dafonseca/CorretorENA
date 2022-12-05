#------------------------------------------------------------------------------#

import sys
sys.path.append('.')

from pathlib import Path

from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import QApplication

import ena_param as ep

from ui.main_window    import MainWindow
from ui.main_controler import MainControler

#------------------------------------------------------------------------------#
def main( argv ):

    try:
        from ctypes import windll
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(ep.MYAPPID)
    except ImportError:
        pass

    icon_file = Path(__file__).resolve().parent / 'resources' / 'icon.ico'

    app = QApplication(argv)
    app.setStyle('fusion')
    app.setWindowIcon(QIcon( str(icon_file) ))
    
    window = MainWindow()
    window.show()

    main_controler = MainControler( window )

    return app.exec()

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    main( sys.argv )

#------------------------------------------------------------------------------#
