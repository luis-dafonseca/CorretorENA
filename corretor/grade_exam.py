#!/usr/bin/python
#------------------------------------------------------------------------------#

import fitz

from registration  import Registration
from progress_bar  import print_progress_bar
from tools         import pix_to_gray_image
from page_ena      import PageENA
from collect_marks import collect_marks
from answers_key   import AnswersKey

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
                grades_xls ):

    reg = create_model_registration( model_pdf )

    n_pages = answers_pdf.page_count

    print_progress_bar( 0, n_pages, fill='*' )
    
    for ii, original_page in enumerate(answers_pdf):
    
        original_pix = original_page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE ) 
        original_img = pix_to_gray_image( original_pix )
    
        image  = reg.transform( original_img )
        marks  = collect_marks( image )
        grades = answers_key.check( marks )

        grades_xls.save_grade( ii, grades.T )
    
        page = PageENA( annotations_pdf )

        page.insert_image ( image )
        page.insert_name  ( grades_xls.get_name(ii) )
        page.insert_annul ( answers_key.keys )
        page.insert_marks ( marks, grades )
        page.insert_grades( grades )

        page.commit()
    
        print_progress_bar( ii+1, n_pages, fill='*' )

#------------------------------------------------------------------------------#
