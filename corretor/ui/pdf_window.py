#------------------------------------------------------------------------------#

from PySide6.QtCore             import QUrl
from PySide6.QtWidgets          import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore    import QWebEngineSettings as settings

#------------------------------------------------------------------------------#
class PDFWindow(QMainWindow):

    #--------------------------------------------------------------------------#
    def __init__( self, parent=None ):

        super().__init__( parent )
 
        self.setWindowTitle('PDF Viewer')
    
        ss = QApplication.primaryScreen().size()
        hh = int( 0.8 * ss.height() )
        ww = int( hh / 297 * 210 )
        xx = ( ss.width () - ww ) // 2
        yy = ( ss.height() - hh ) // 2
        self.setGeometry( xx, yy, ww, hh )
 
        self._webView = QWebEngineView()

        self._webView.settings().setAttribute( settings.PluginsEnabled,            True  )
        self._webView.settings().setAttribute( settings.AutoLoadIconsForPage,      False )
        self._webView.settings().setAttribute( settings.AutoLoadImages,            False )
        self._webView.settings().setAttribute( settings.ErrorPageEnabled,          False )
        self._webView.settings().setAttribute( settings.JavascriptCanOpenWindows,  False )
        self._webView.settings().setAttribute( settings.JavascriptEnabled,         False )
        self._webView.settings().setAttribute( settings.LinksIncludedInFocusChain, False )
        self._webView.settings().setAttribute( settings.LocalStorageEnabled,       False )
        self._webView.settings().setAttribute( settings.NavigateOnDropEnabled,     False )
        self._webView.settings().setAttribute( settings.ShowScrollBars,            False )
        self._webView.settings().setAttribute( settings.WebGLEnabled,              False )

        self.setCentralWidget(self._webView)
 
    #--------------------------------------------------------------------------#
    def load( self, file_location, toolbar=False ):

        tb = '' if toolbar else '#toolbar=0'

        self._webView.load( QUrl(f'file://{file_location}{tb}') )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    import os
    import sys
    
    os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--disable-logging'

    app = QApplication(sys.argv)
    win = PDFWindow()

    win.load('/home/luis/01-Work/03-profmat/07-Corretor_ENA/corretor-git/docs/example/exemplo-respostas.pdf')
    win.show()

    sys.exit( app.exec() )
