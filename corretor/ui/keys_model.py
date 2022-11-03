#!/usr/bin/python
#------------------------------------------------------------------------------#

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui  import QRegularExpressionValidator, QFontDatabase

from grading.answers_key import AnswersKey

#------------------------------------------------------------------------------#
def str_to_key( s ):
    return ''.join(s.split())

#------------------------------------------------------------------------------#
class KeysModel:

    #--------------------------------------------------------------------------#
    def __init__(self, s='A'*30 ):

        self.keys = str_to_key(s)
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
    def answers_key( self ):
        return AnswersKey( self.keys )

#------------------------------------------------------------------------------#
