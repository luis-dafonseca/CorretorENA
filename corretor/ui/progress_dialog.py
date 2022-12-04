#------------------------------------------------------------------------------#

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QProgressDialog

#------------------------------------------------------------------------------#
class ProgressDialog:

    #--------------------------------------------------------------------------#
    def __init__( self, parent, title ):

        self.progress = QProgressDialog( 'Corrigindo...', 'Cancelar', 0, 1, parent )

        self.progress.setWindowTitle(title)
        self.progress.setWindowModality(Qt.WindowModal)
        self.progress.setMinimumDuration(0)

    #--------------------------------------------------------------------------#
    def start( self, total ):

        self.value = 0
        self.total = total

        self.progress.setRange( 0, total )
        self.progress.setValue(self.value)

    #--------------------------------------------------------------------------#
    def step(self):

        self.value += 1
        self.progress.setValue(self.value)

        if self.progress.wasCanceled():
            self.progress.setValue(self.total)
            return False
        else:
            return True

#------------------------------------------------------------------------------#
