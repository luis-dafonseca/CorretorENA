#------------------------------------------------------------------------------#

from PySide6.QtWidgets  import QDialog, QDialogButtonBox
from ui.form_show_names import Ui_ShowNames

#------------------------------------------------------------------------------#
def show_names( parent, filename, first_name, names ):

    dialog = QDialog(parent)
    dialog.ui = Ui_ShowNames()
    dialog.ui.setupUi(dialog)

    dialog.ui.labelFileName .setText( filename   )
    dialog.ui.labelFirstName.setText( first_name )
    
    label_name = [ dialog.ui.labelName_1,
                   dialog.ui.labelName_2,
                   dialog.ui.labelName_3,
                   dialog.ui.labelName_4,
                   dialog.ui.labelName_5,
                   dialog.ui.labelName_6 ]

    label_number = [ dialog.ui.labelNumber_1,
                     dialog.ui.labelNumber_2,
                     dialog.ui.labelNumber_3,
                     dialog.ui.labelNumber_4,
                     dialog.ui.labelNumber_5,
                     dialog.ui.labelNumber_6 ]

    N = len(names)

    if N <= 6:

        for nn in range(N):
            label_name[nn].setText( names[nn] )

        for nn in range(N,6):
            label_name  [nn].hide()
            label_number[nn].hide()
        
        dialog.ui.labelEllipsis.hide()

    else:

        for nn in range(3):
            label_name[nn].setText( names[nn] )

        for nn in range(-1,-4,-1):
            label_name  [nn].setText( names[nn] )
            label_number[nn].setText( str(N+1+nn) )

    dialog.ui.buttonBox.button( QDialogButtonBox.Cancel ).hide()
    dialog.resize( 1, 1 )
    dialog.exec()

#------------------------------------------------------------------------------#
