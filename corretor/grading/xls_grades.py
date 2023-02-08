#------------------------------------------------------------------------------#

from openpyxl            import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
from openpyxl.styles     import Font, Alignment

import ena_param as ep

#------------------------------------------------------------------------------#
class XLSGrades:

    #--------------------------------------------------------------------------#
    def __init__(self, fname):

        self.fname = fname

        self.wb    = Workbook()
        self.sheet = self.wb.active

        self.sheet['A1'] = 'Nome'
        self.sheet['B1'] = 'Nota'
        self.sheet['C1'] = 'Status'

        self.sheet['A1'].alignment = Alignment(horizontal='center')
        self.sheet['B1'].alignment = Alignment(horizontal='center')
        self.sheet['C1'].alignment = Alignment(horizontal='center')

        self.sheet['A1'].font = Font(bold=True)
        self.sheet['B1'].font = Font(bold=True)
        self.sheet['C1'].font = Font(bold=True)

        self.sheet.column_dimensions['A'].width = 16
        self.sheet.column_dimensions['C'].width = 12

        self.min_score = ep.MIN_SCORE

        self.has_names = False

    #--------------------------------------------------------------------------#
    def write_names(self, names):

        ww = 4

        for rr, name in enumerate(names):
            name = name.strip()
            ww = max( ww, len(name) )
            self.sheet.cell(row=rr+2,column=1).value = name

        self.sheet.column_dimensions['A'].width = ww * 1.6

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
    def add_grade(self, ii, eliminated, absent, grade ):

        aa = self.sheet.cell( ii+2, 1 )
        bb = self.sheet.cell( ii+2, 2 )
        cc = self.sheet.cell( ii+2, 3 )

        if not self.has_names:
            aa.value = str(f'Candidato {ii+1}')

        bb.value     = grade
        bb.alignment = Alignment(horizontal='center')

        if eliminated:
            cc.value = 'Eliminado'
        elif absent:
            cc.value = 'Ausente'
        elif grade >= self.min_score:
            cc.value = 'Aprovado'
        else:
            cc.value = 'Reprovado'

    #--------------------------------------------------------------------------#
    def reset(self):
        '''Remove all names, grades and status.'''

        for row in self.sheet.iter_rows( min_row=1 ):
            for cell in row:
                cell.value = None

    #--------------------------------------------------------------------------#
    def save(self):
        self.wb.save( self.fname )

#------------------------------------------------------------------------------#

