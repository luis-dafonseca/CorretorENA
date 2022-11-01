#------------------------------------------------------------------------------#

import fitz

from openpyxl import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

from grading.grade_exam  import grade_exam
from grading.answers_key import AnswersKey
from grading.xls_grades  import XLSGrades
from grading.page_ena    import PageENA
from grading.tools       import pix_to_gray_image

_DPI        = 300
_COLORSPACE = "GRAY"

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
        self.has_keys        = False
        self.has_names       = False
        
        self.names = []

        self._model       = None
        self._answers     = None
        self._annotations = None
        self._grades      = None
        self._keys        = ''

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
                    self._keys, 
                    self._answers, 
                    self._annotations, 
                    self._grades,
                    self._progress_bar )
        
        self._annotations.save( self._fname_annotations )
        self._grades     .save()

    #--------------------------------------------------------------------------#
    def ready_to_run(self):
        return self.has_model       and \
               self.has_keys        and \
               self.has_answers     and \
               self.has_annotations and \
               self.has_grades

    #--------------------------------------------------------------------------#
    def set_model( self, fname ):       
        if self.has_model:
            self._model.close()

        self._model = fitz.open( fname )
        self.has_model  = True

    #--------------------------------------------------------------------------#
    def set_keys( self, keys ):        
        self._keys = AnswersKey( keys )
        self.has_keys     = True

    #--------------------------------------------------------------------------#
    def set_answers( self, fname ):     
        if self.has_answers:
            self._answers.close()

        self._answers    = fitz.open( fname )
        self.has_answers = True

    #--------------------------------------------------------------------------#
    def set_names( self, fname, first_name ):       

        xls   = load_workbook(fname)
        sheet = xls.active

        xy = coordinate_from_string(first_name) 
        cc = column_index_from_string(xy[0]) - 1
        ll = xy[1]

        self.names = []

        for rr, row in enumerate( sheet.iter_rows(min_row=ll, values_only=True) ):
            self.names.append(row[cc])

        xls.close()

        self.has_names = True

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
    def get_pix_model(self):      

        model_page = self._model.load_page(0)
        model_pix  = model_page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE )
        image      = pix_to_gray_image( model_pix )

        page = PageENA( fitz.open() )

        page.create_page ()
        page.insert_image( image )
        page.insert_rects()

        page.commit()

        pix = page.page.get_pixmap()

        return pix

    #--------------------------------------------------------------------------#
    def get_pix_keys(self):      

        model_page = self._model.load_page(0)
        model_pix  = model_page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE )
        image      = pix_to_gray_image( model_pix )

        page = PageENA( fitz.open() )

        page.create_page ()
        page.insert_image( image )
        page.insert_rects()

        page.commit()

        pix = page.page.get_pixmap()

        return pix

#------------------------------------------------------------------------------#