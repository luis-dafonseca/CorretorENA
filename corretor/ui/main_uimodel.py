#------------------------------------------------------------------------------#

import os
import fitz
import tempfile

from openpyxl            import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

import grading.ena_param  as ep
from   grading.grade_exam import grade_exam
from   grading.xls_grades import XLSGrades
from   grading.page_ena   import PageENA
from   grading.grades     import keys_str_to_list
from   ui.keys_model      import KeysModel

#------------------------------------------------------------------------------#
class UIProgressBar:

    #--------------------------------------------------------------------------#
    def __init__(self,progress_bar):
        self.progress_bar = progress_bar

    #--------------------------------------------------------------------------#
    def start(self,N):
        self.value     = 0
        self.increment = 100/N

    #--------------------------------------------------------------------------#
    def step(self):
        self.value += self.increment
        self.progress_bar.setValue(self.value)

#------------------------------------------------------------------------------#
class MainUIModel:

    #--------------------------------------------------------------------------#
    def __init__(self, progress_bar):

        self.has_model       = False
        self.has_answers     = False
        self.has_annotations = False
        self.has_grades      = False
        self.has_names       = False
        
        self.names = []

        self._model       = None
        self._answers     = None
        self._annotations = None
        self._grades      = None

        self._answers_fname = ''

        self.keys_model = KeysModel()

        self._progress_bar = UIProgressBar(progress_bar)

    #--------------------------------------------------------------------------#
    def __del__(self):

        if self.has_model:
            self._model.close()

        if self.has_answers:
            self._answers.close()

    #--------------------------------------------------------------------------#
    def run(self):

        if self.has_names:
            self._grades.add_names(self.names)

        grade_exam( self._model, 
                    self.keys_model.keys, 
                    self._answers, 
                    self._annotations, 
                    self._grades,
                    self._progress_bar )
        
        self._annotations.save( self._fname_annotations )
        self._grades     .save()

    #--------------------------------------------------------------------------#
    def ready_to_run(self):
        return self.has_model       and \
               self.has_answers     and \
               self.has_annotations and \
               self.has_grades

    #--------------------------------------------------------------------------#
    def set_model( self, fname ):       

        new_model = fitz.open( fname )
        
        if new_model.page_count != 1:
            raise ValueError( f'{fname} não contém um modelo' )

        if self.has_model:
            self._model.close()

        self._model    = new_model
        self.has_model = True

    #--------------------------------------------------------------------------#
    def set_answers( self, fname ):     
        if self.has_answers:
            self._answers.close()

        self._answers       = fitz.open( fname )
        self._answers_fname = os.path.abspath( fname )
        self.has_answers    = True

    #--------------------------------------------------------------------------#
    def set_names( self, fname, first_name ):       

        xls   = load_workbook(fname)
        sheet = xls.active

        xy = coordinate_from_string(first_name) 
        cc = column_index_from_string(xy[0]) - 1
        ll = xy[1]

        self.names = []

        for rr, row in enumerate( sheet.iter_rows(min_row=ll, values_only=True) ):
            self.names.append( str(row[cc]).strip() )

        xls.close()

        self.has_names = True

    #--------------------------------------------------------------------------#
    def remove_names( self ):       
        self.names     = []
        self.has_names = False

    #--------------------------------------------------------------------------#
    def set_annotations( self, fname ): 
        self._fname_annotations = fname
        self._annotations       = fitz.open()
        self.has_annotations    = True

    #--------------------------------------------------------------------------#
    def set_grades( self, fname ):      
        self._grades    = XLSGrades( fname )
        self.has_grades = True

    #--------------------------------------------------------------------------#
    def get_model_pdf(self):      

        pixmap = self._model[0].get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )

        new_pdf = fitz.open() 

        page = PageENA( new_pdf )
        page.create_page()
        page.insert_pixmap( pixmap )
        page.draw_all_rects()
        page.commit()

        self._temp_file = tempfile.NamedTemporaryFile()
        new_pdf.save( self._temp_file.name )

        return self._temp_file.name

    #--------------------------------------------------------------------------#
    def get_keys_pdf(self):      

        pixmap = self._model[0].get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )

        new_pdf = fitz.open() 

        page = PageENA( new_pdf )
        page.create_page()
        page.insert_pixmap( pixmap )
        page.draw_answers_key( keys_str_to_list( self.keys_model.keys ) )
        page.commit()

        self._temp_file = tempfile.NamedTemporaryFile()
        new_pdf.save( self._temp_file.name )

        return self._temp_file.name

    #--------------------------------------------------------------------------#
    def get_answers_pdf(self):      
        return self._answers_fname

#------------------------------------------------------------------------------#
