#------------------------------------------------------------------------------#
'''Define answer keys validator, mask and regular expression'''

from PySide6.QtCore    import QRegularExpression
from PySide6.QtWidgets import QWidget
from PySide6.QtGui     import (QRegularExpressionValidator, QFont)

#------------------------------------------------------------------------------#

# Monospace font to key line edit
FONT = QFont("Monospace")

# Keys line edit mask
MASK = '>'+(' '+'A'*5)*6

#------------------------------------------------------------------------------#
def validator(parent: QWidget) -> QRegularExpressionValidator:
    '''Return the regular expression validator for line edit keys'''

    REGEX = QRegularExpression((' '+'[ABCDEX]'*5)*6)

    return QRegularExpressionValidator(REGEX, parent)

#------------------------------------------------------------------------------#