#!/usr/bin/python
#------------------------------------------------------------------------------#

import fitz

from grading.registration  import Registration
from grading.tools         import pix_to_gray_image
from grading.page_ena      import PageENA
from grading.collect_marks import collect_marks
from grading.answers_key   import AnswersKey

_DPI        = 300
_COLORSPACE = "GRAY"

#------------------------------------------------------------------------------#
def create_model_registration( model_pdf ):

    page = model_pdf[0]

    pix = page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE )

    image = pix_to_gray_image( pix )
    
    return Registration( image )

#------------------------------------------------------------------------------#
def grade_exam( model_pdf, 
                answers_key, 
                answers_pdf, 
                annotations_pdf, 
                grades_xls,
                progress_bar):

    reg = create_model_registration( model_pdf )

    progress_bar.start( answers_pdf.page_count )
    
    for ii, original_page in enumerate(answers_pdf):
    
        original_pix = original_page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE ) 
        original_img = pix_to_gray_image( original_pix )
    
        image  = reg.transform( original_img )
        marks  = collect_marks( image )
        grades = answers_key.check( marks )

        grades_xls.add_grade( ii, grades.T )
    
        page = PageENA( annotations_pdf )

        page.insert_image ( image )
        page.insert_name  ( grades_xls.get_name(ii) )
        page.insert_annul ( answers_key.keys )
        page.insert_marks ( marks, grades )
        page.insert_grades( grades )

        page.commit()
    
        progress_bar.step()

#------------------------------------------------------------------------------#
