#------------------------------------------------------------------------------#
'''Create a Progress Bar class'''

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QProgressDialog

#------------------------------------------------------------------------------#
class ProgressDialog:
    '''Progress Bar class using QProgressDialog'''

    #--------------------------------------------------------------------------#
    def __init__( self, parent, title ) -> None:
        '''Initialize Progress Bar instance'''

        self.progress = QProgressDialog(
            'Corrigindo...',
            'Cancelar',
            0,
            1,
            parent
        )

        self.progress.setWindowTitle(title)
        self.progress.setWindowModality(Qt.WindowModal)
        self.progress.setMinimumDuration(0)

    #--------------------------------------------------------------------------#
    def start(self, total_of_steps: int) -> None:

        self.value = 0
        self.total = total_of_steps

        self.progress.setRange(0, total_of_steps)
        self.progress.setValue(self.value)

    #--------------------------------------------------------------------------#
    def step(self) -> bool:
        '''Progress one step and check if user canceled the correction

        Return:
            False if user canceled the correction
        '''

        self.value += 1
        self.progress.setValue(self.value)

        if self.progress.wasCanceled():
            self.progress.setValue(self.total)
            return False
        else:
            return True

#------------------------------------------------------------------------------#
