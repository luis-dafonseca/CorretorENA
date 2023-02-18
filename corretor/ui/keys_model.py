#------------------------------------------------------------------------------#
'''Define keys dialog interface model '''

from pathlib import Path

from PySide6.QtCore    import QRegularExpression
from PySide6.QtWidgets import QWidget
from PySide6.QtGui     import(QRegularExpressionValidator, QFontDatabase)

import ena_param as ep

N_QUESTIONS = 30

#------------------------------------------------------------------------------#
def parse_keys_str(s: str) -> str:
    '''Parse keys string to remove spaces and convert all chars to uppercase'''

    return (''.join(s.split())).upper()

#------------------------------------------------------------------------------#
class KeysModel:
    '''Keys dialog interface model class'''

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:
        '''Initialize key dialog model instance'''

        self.ena_keys = ep.ENA_KEYS

        self.keys = 'A' * N_QUESTIONS
        self.keys_next = self.keys

        self.mask  = '>'+(' '+'A'*5)*6
        self.regex = QRegularExpression((' '+'[ABCDEX]'*5)*6)
        self.font  = QFontDatabase.systemFont(QFontDatabase.FixedFont)

    #--------------------------------------------------------------------------#
    def update(self) -> None:
        '''Update the keys set on accepting edition'''

        self.keys = self.keys_next

    #--------------------------------------------------------------------------#
    def reset(self) -> None:
        '''Reset next keys string'''

        self.keys_next = self.keys

    #--------------------------------------------------------------------------#
    def validator(self, parent: QWidget) -> QRegularExpressionValidator:
        '''Return the regular expression validator for line edit keys'''

        return QRegularExpressionValidator(self.regex, parent)

    #--------------------------------------------------------------------------#
    def set_key(self, ii: int, kk: str) -> None:
        '''Set ii key value to kk'''

        self.keys_next = self.keys_next[:ii] + kk + self.keys_next[ii+1:]

    #--------------------------------------------------------------------------#
    def set_keys(self, new_keys: str) -> None:
        '''Define new key values to new_keys'''

        self.keys_next = parse_keys_str(new_keys)

    #--------------------------------------------------------------------------#
    def set_ena_keys(self, year: int) -> str:
        '''Define new key values to keys from ENA of year'''

        self.keys      = self.ena_keys[year]
        self.keys_next = self.keys

        return self.keys

    #--------------------------------------------------------------------------#
    def get_ena_years(self) -> list[int]:
        '''Return the list of years of stored ENA keys'''

        return self.ena_keys.keys()

    #--------------------------------------------------------------------------#
    def read_keys(self, filename: str) -> str:
        '''Read answer keys from TXT file'''

        with open(filename) as file:
            contents = file.readlines()

        name    = Path(filename).name
        message = f'O arquivo {name} não contém um gabarito!'

        if len(contents) != 1:
            raise ValueError(message)

        str_keys = parse_keys_str(contents[0])

        if len(str_keys) != 30:
            raise ValueError(message)

        aa = set('ABCDEX')
        ss = set(str_keys)

        if not ss.issubset(aa):
            raise ValueError(message)

        self.keys      = str_keys
        self.keys_next = str_keys

        return str_keys

    #--------------------------------------------------------------------------#
    def write_keys( self, filename ) -> None:
        with open( filename, 'w' ) as f:
             f.write( self.keys )

#------------------------------------------------------------------------------#
