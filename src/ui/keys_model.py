#------------------------------------------------------------------------------#
'''Define keys dialog interface model '''

from pathlib import Path

import ena_param as ep

N_QUESTIONS = 30

#------------------------------------------------------------------------------#
class KeysModel:
    '''Keys dialog interface model class'''

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:
        '''Initialize key dialog model instance'''

        self.ena_keys = ep.ENA_KEYS

        self.keys = 'A' * N_QUESTIONS
        self.keys_next = self.keys

        self.fname = ''

    #--------------------------------------------------------------------------#
    def parse_keys_str(self, keys: str) -> str:
        '''Remove spaces and convert string to uppercase'''

        return (''.join(keys.split())).upper()

    #--------------------------------------------------------------------------#
    def get_keys(self) -> str:
        '''Return keys string'''

        return self.keys

    #--------------------------------------------------------------------------#
    def update(self) -> None:
        '''Update the keys set on accepting edition'''

        self.keys = self.keys_next

    #--------------------------------------------------------------------------#
    def reset(self) -> None:
        '''Reset next keys string'''

        self.keys_next = self.keys

    #--------------------------------------------------------------------------#
    def set_key(self, ii: int, kk: str) -> None:
        '''Set ii key value to kk'''

        self.keys_next = self.keys_next[:ii] + kk + self.keys_next[ii+1:]

    #--------------------------------------------------------------------------#
    def set_keys(self, new_keys: str) -> None:
        '''Define new key values'''

        self.keys_next = self.parse_keys_str(new_keys)
        self.keys      = self.keys_next

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
    def read_keys(self, fname: str) -> str:
        '''Read answer keys from TXT file'''

        with open(fname) as file:
            contents = file.readlines()

        name    = Path(fname).name
        message = f'O arquivo {name} não contém um gabarito!'

        if len(contents) != 1:
            raise ValueError(message)

        str_keys = self.parse_keys_str(contents[0])

        if len(str_keys) != 30:
            raise ValueError(message)

        aa = set('ABCDEX')
        ss = set(str_keys)

        if not ss.issubset(aa):
            raise ValueError(message)

        self.keys      = str_keys
        self.keys_next = str_keys

        self.fname = fname

        return str_keys

    #--------------------------------------------------------------------------#
    def write_keys(self) -> None:
        '''Write answer keys from TXT file'''

        with open(self.fname, 'w') as file:
            file.write(self.keys)

#------------------------------------------------------------------------------#
