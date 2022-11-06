#------------------------------------------------------------------------------#

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui  import QRegularExpressionValidator, QFontDatabase

import grading.ena_param   as ep
from   grading.answers_key import AnswersKey

#------------------------------------------------------------------------------#
def str_to_key( s ):
    return ''.join(s.split())

#------------------------------------------------------------------------------#
class KeysModel:

    #--------------------------------------------------------------------------#
    def __init__(self):

        self.ena_keys = ep.ENA_KEYS

        self.keys = 'A'*ep.N_QUESTIONS
        self.keys_next = self.keys

        self.mask  = '>'+(' '+'A'*5)*6
        self.regex = QRegularExpression((' '+'[ABCDEX]'*5)*6)
        self.font  = QFontDatabase.systemFont(QFontDatabase.FixedFont)

    #--------------------------------------------------------------------------#
    def update( self ):
        self.keys = self.keys_next

    #--------------------------------------------------------------------------#
    def reset( self ):
        self.keys_next = self.keys

    #--------------------------------------------------------------------------#
    def validator( self, parent ):
        return QRegularExpressionValidator( self.regex, parent )

    #--------------------------------------------------------------------------#
    def set_key( self, ii, cc ):
        self.keys_next = self.keys_next[:ii] + cc + self.keys_next[ii+1:]

    #--------------------------------------------------------------------------#
    def set_keys( self, s ):
        self.keys_next = str_to_key(s)

    #--------------------------------------------------------------------------#
    def set_ena_keys( self, yy ):
        self.keys      = self.ena_keys[yy]
        self.keys_next = self.keys
        return self.keys

    #--------------------------------------------------------------------------#
    def get_ena_years( self ):
        return self.ena_keys.keys()

    #--------------------------------------------------------------------------#
    def answers_key( self ):
        return AnswersKey( self.keys )

#------------------------------------------------------------------------------#
