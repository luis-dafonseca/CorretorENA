#------------------------------------------------------------------------------#

from openpyxl import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

#------------------------------------------------------------------------------#
class XLSGrades:

    #--------------------------------------------------------------------------#
    def __init__(self, fname):

        self.fname = fname

        self.wb    = Workbook()
        self.sheet = self.wb.active

        self.sheet['A1'] = 'Nome'
        self.sheet['B1'] = 'Nota'

        self.has_names = False

    #--------------------------------------------------------------------------#
    def add_names(self, names):
        
        for rr, name in enumerate(names):
            self.sheet.cell(row=rr+2,column=1).value = name

        self.has_names = True

    #--------------------------------------------------------------------------#
    def read_names(self, fname, first_name):

        xls   = load_workbook(fname)
        sheet = xls.active

        xy = coordinate_from_string(first_name) 
        cc = column_index_from_string(xy[0]) - 1
        ll = xy[1]

        for rr, row in enumerate( sheet.iter_rows( min_row=ll, values_only=True )):

            self.sheet.cell(row=rr+2,column=1).value = row[cc]

        xls.close()

        self.has_names = True

    #--------------------------------------------------------------------------#
    def get_name(self, ii):

        if self.has_names:
            return str(self.sheet.cell(row=ii+2, column=1).value)
        else:
            return str(f'Candidato {ii+1}')
    
    #--------------------------------------------------------------------------#
    def add_grade(self, ii, grade):

        if not self.has_names:
            self.sheet.cell(row=ii+2, column=1).value = str(f'Candidato {ii+1}')

        self.sheet.cell(row=ii+2, column=2).value = grade

    #--------------------------------------------------------------------------#
    def save(self):
        self.wb.save( self.fname )

#------------------------------------------------------------------------------#

