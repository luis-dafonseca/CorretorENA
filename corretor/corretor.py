#------------------------------------------------------------------------------#

import sys
sys.path.append('.')

from PySide6.QtWidgets import QApplication
from ui.main_window    import MainWindow
from ui.main_controler import MainControler

#------------------------------------------------------------------------------#
def main( argv ):

    app = QApplication(argv)
    QApplication.setStyle('fusion')
    
    window = MainWindow()
    window.show()

    main_controler = MainControler( window )

    return app.exec()

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    main( sys.argv )

#------------------------------------------------------------------------------#
