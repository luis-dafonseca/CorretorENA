#------------------------------------------------------------------------------#

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui  import QRegularExpressionValidator, QFontDatabase

import grading.ena_param as ep

#------------------------------------------------------------------------------#
def str_to_key( s ):
    return ( ''.join(s.split()) ).upper()

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
    def read_keys( self, filename ):

        with open(filename) as f:
            contents = f.readlines()
        
        if len(contents) != 1:
            raise ValueError( f'{filename} não contém um gabarito' )
        
        str_keys = str_to_key( contents[0] )
        
        if len(str_keys) != 30:
            raise ValueError( f'{filename} não contém um gabarito' )

        aa = set( 'ABCDEX' )
        ss = set( str_keys )
        
        if not ss.issubset(ss):
            raise ValueError( f'{filename} não contém um gabarito' )

        self.keys      = str_keys
        self.keys_next = str_keys

        return str_keys

#------------------------------------------------------------------------------#
