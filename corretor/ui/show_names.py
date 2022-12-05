#------------------------------------------------------------------------------#

from PySide6.QtWidgets  import QDialog, QDialogButtonBox
from ui.form_show_names import Ui_ShowNames

#------------------------------------------------------------------------------#
def ShowNamesWindow( parent, filename, first_name, names ):

    dialog = QDialog(parent)
    dialog.ui = Ui_ShowNames()
    dialog.ui.setupUi(dialog)

    dialog.ui.labelFileName .setText( filename   )
    dialog.ui.labelFirstName.setText( first_name )

    dialog.ui.labelName_1.setText( names[ 0] )
    dialog.ui.labelName_2.setText( names[ 2] )
    dialog.ui.labelName_3.setText( names[ 3] )
    dialog.ui.labelName_4.setText( names[-3] )
    dialog.ui.labelName_5.setText( names[-2] )
    dialog.ui.labelName_6.setText( names[-1] )

    N = len(names)
    dialog.ui.labelNumber_4.setText( str(N-2) )
    dialog.ui.labelNumber_5.setText( str(N-1) )
    dialog.ui.labelNumber_6.setText( str(N  ) )

    dialog.ui.buttonBox.button( QDialogButtonBox.Cancel ).hide()
    dialog.exec()

#------------------------------------------------------------------------------#
