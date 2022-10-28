#------------------------------------------------------------------------------#

from openpyxl import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

#------------------------------------------------------------------------------#
class XLSGrades:

    #--------------------------------------------------------------------------#
    def __init__(self, fname=None, cell='A2'):

        self.wb    = Workbook()
        self.sheet = self.wb.active

        self.sheet['A1'] = 'Nome'
        self.sheet['B1'] = 'Nota'

        if fname:

            input_xls   = load_workbook(fname)
            input_sheet = input_xls.active

            xy = coordinate_from_string(cell) 
            cc = column_index_from_string(xy[0])
            ll = xy[1]

            for rr, row in enumerate( input_sheet.iter_rows( min_row=ll, values_only=True )):

                self.sheet.cell(row=rr+2,column=1).value = row[cc-1]

            input_xls.close()

    #--------------------------------------------------------------------------#
    def get_name(self, ii):
        return str(self.sheet.cell(row=ii+2, column=1).value)
    
    #--------------------------------------------------------------------------#
    def save_grade(self, ii, grade):
        if not self.sheet.cell(row=ii+2, column=1).value:
            self.sheet.cell(row=ii+2, column=1).value = ii+1

        self.sheet.cell(row=ii+2, column=2).value = grade

    #--------------------------------------------------------------------------#
    def save(self, fname):
        self.wb.save( fname )

#------------------------------------------------------------------------------#

if __name__ == "__main__":

    xls = XLSGrades()

    for ii in range(10):
        xls.save_grade( ii, 100+ii )

    xls.save('test-1.xlsx')

    xls = XLSGrades('../../pdf/exemplo.xlsx', 'A2')

    for ii in range(10):
        xls.save_grade( ii, 100+ii )

    xls.save('test-2.xlsx')

#------------------------------------------------------------------------------#
