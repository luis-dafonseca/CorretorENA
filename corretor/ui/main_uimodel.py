#------------------------------------------------------------------------------#

import os
import fitz
import tempfile
from pathlib import Path

from openpyxl            import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

import ena_param as ep

from grading.grade_exam import grade_exam
from grading.xls_grades import XLSGrades
from grading.page_ena   import PageENA
from grading.grades     import keys_str_to_list

from ui.keys_model      import KeysModel

#------------------------------------------------------------------------------#
class MainUIModel:

    #--------------------------------------------------------------------------#
    def __init__( self ):

        self.has_model       = False
        self.has_answers     = False
        self.has_annotations = False
        self.has_grades      = False
        self.has_names       = False
        
        self.names = []

        self.model       = None
        self.answers     = None
        self.annotations = None
        self.grades      = None

        self.num_answers = 0
        self.num_names   = 0

        self.answers_fname = ''

        self.keys_model = KeysModel()

    #--------------------------------------------------------------------------#
    def __del__(self):

        if self.has_model:
            self.model.close()

        if self.has_answers:
            self.answers.close()

    #--------------------------------------------------------------------------#
    def run( self, progress ):

        if self.has_names:
            self.grades.add_names(self.names)

        finished = grade_exam( self.model, 
                               self.keys_model.keys, 
                               self.answers, 
                               self.annotations, 
                               self.grades,
                               progress )
       
        if finished:
            self.annotations.save( self.fname_annotations )
            self.grades     .save()

        return finished

    #--------------------------------------------------------------------------#
    def ready_to_run(self):
        return self.has_model       and \
               self.has_answers     and \
               self.has_annotations and \
               self.has_grades

    #--------------------------------------------------------------------------#
    def set_model( self, fname ):       

        name = Path(fname).name

        try:
            new_model = fitz.open( fname )
        except:
            raise ValueError( f'O arquivo {name} não pôde ser aberto!\n' )
        
        nn = new_model.page_count

        if nn == 0:
            raise ValueError( f'O arquivo {name} não é um modelo!\n\nEle não contém nenhuma página.\n' )
        elif nn > 1:
            raise ValueError( f'O arquivo {name} não é um modelo!\n\nEle contém mais do que uma página.\n' )

        if self.has_model:
            self.model.close()

        self.model     = new_model
        self.has_model = True

    #--------------------------------------------------------------------------#
    def set_answers( self, fname ):     

        name = Path(fname).name

        try:
            new_answers = fitz.open( fname )
        except:
            raise ValueError( f'O arquivo {name} não pôde ser aberto!\n' )

        nn = new_answers.page_count
        
        if nn == 0:
            raise ValueError( f'O arquivo {name} não contém nenhuma página.\n' )
        
        if self.has_answers:
            self.answers.close()

        self.num_answers   = nn
        self.answers       = new_answers
        self.answers_fname = os.path.abspath( fname )
        self.has_answers   = True

        if self.has_names and ( self.num_answers != self.num_names ):
            raise IndexError( f'Cuidado: A quantidade de respostas ({self.num_answers}) não coincide com a quantidade de nomes ({self.num_names}).\n' )

    #--------------------------------------------------------------------------#
    def set_names( self, fname, first_name ):       

        name = Path(fname).name

        try:
            xls = load_workbook(fname)
        except:
            raise ValueError( f'O arquivo {name} não pôde ser aberto!\n' )

        try:
            sheet = xls.active

            xy = coordinate_from_string(first_name) 
            cc = column_index_from_string(xy[0]) - 1
            ll = xy[1]

            self.names = []

            for rr, row in enumerate( sheet.iter_rows(min_row=ll, values_only=True) ):
                self.names.append( str(row[cc]).strip() )

            xls.close()

        except:
            self.names = []
            raise ValueError( f'Não foi possível ler os nomes do arquivo {name}!\n' )

        self.num_names = len(self.names)
        self.has_names = True

        if self.has_answers and ( self.num_answers != self.num_names ):
            raise IndexError( f'Cuidado: A quantidade de respostas ({self.num_answers}) não coincide com a quantidade de nomes ({self.num_names}).\n' )

    #--------------------------------------------------------------------------#
    def remove_names( self ):       
        self.names     = []
        self.num_names = 0
        self.has_names = False

    #--------------------------------------------------------------------------#
    def set_annotations( self, fname ): 

        try:
            self.annotations = fitz.open()
        except:
            raise ValueError( f'O arquivo {Path(fname).name} não pôde ser aberto!\n' )

        self.fname_annotations = fname
        self.has_annotations   = True

    #--------------------------------------------------------------------------#
    def set_grades( self, fname ):      

        try:
            self.grades = XLSGrades( fname )
        except:
            raise ValueError( f'O arquivo {Path(fname).name} não pôde ser aberto!\n' )

        self.has_grades = True

    #--------------------------------------------------------------------------#
    def get_model_pdf(self):      

        pixmap = self.model[0].get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )

        new_pdf = fitz.open() 

        page = PageENA( new_pdf )
        page.create_page()
        page.insert_pixmap( pixmap )
        page.draw_all_rects()
        page.commit()

        self.temp_file = tempfile.NamedTemporaryFile( prefix='modelo_', suffix='.pdf' )
        new_pdf.save( self.temp_file.name )

        return self.temp_file.name

    #--------------------------------------------------------------------------#
    def get_keys_pdf(self):      

        pixmap = self.model[0].get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )

        new_pdf = fitz.open() 

        page = PageENA( new_pdf )
        page.create_page()
        page.insert_pixmap( pixmap )
        page.draw_answers_key( keys_str_to_list( self.keys_model.keys ) )
        page.commit()

        self.temp_file = tempfile.NamedTemporaryFile( prefix='gabarito_', suffix='.pdf' )
        new_pdf.save( self.temp_file.name )

        return self.temp_file.name

    #--------------------------------------------------------------------------#
    def get_answers_pdf(self):      
        return self.answers_fname

#------------------------------------------------------------------------------#
