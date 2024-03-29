#------------------------------------------------------------------------------#
'''CorretorENA main module'''


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import QApplication

import ena_param as ep

from ui.main_window     import MainWindow
from ui.main_controller import MainController

#------------------------------------------------------------------------------#
def main(argv):

    try:
        from ctypes import windll
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(ep.MY_APP_ID)
    except ImportError:
        pass

    icon_file = ep.RESOURCES / 'icon.ico'

    app = QApplication(argv)
    app.setStyle('fusion')
    app.setWindowIcon(QIcon(str(icon_file)))

    window = MainWindow()
    window.resize(539, 658)

    main_controller = MainController(window)

    window.show()

    return app.exec()

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    main( sys.argv )

#------------------------------------------------------------------------------#
