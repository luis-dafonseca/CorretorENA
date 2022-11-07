#------------------------------------------------------------------------------#

import fitz

import grading.ena_param    as ep
from   grading.registration import Registration
from   grading.tools        import pix_to_gray_image
from   grading.page_ena     import PageENA
from   grading.marks        import collect_marks
from   grading.grades       import check_answers, keys_str_to_list

#------------------------------------------------------------------------------#
def create_model_registration( model_pdf ):

    page = model_pdf[0]

    pix = page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )

    image = pix_to_gray_image( pix )
    
    return Registration( image )

#------------------------------------------------------------------------------#
def grade_exam( model_pdf, 
                keys, 
                answers_pdf, 
                annotations_pdf, 
                grades_xls,
                progress_bar):

    reg = create_model_registration( model_pdf )

    k_lst = keys_str_to_list( keys )

    progress_bar.start( answers_pdf.page_count )
    
    for ii, original_page in enumerate(answers_pdf):
    
        original_pix = original_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE ) 
        original_img = pix_to_gray_image( original_pix )
    
        image  = reg.transform( original_img )
        marks  = collect_marks( image )
        grades = check_answers( marks, k_lst )

        grades_xls.add_grade( ii, marks.eliminated, marks.absent, grades.total )
    
        page = PageENA( annotations_pdf )
        page.create_page  ()
        page.insert_image ( image )
        page.insert_name  ( grades_xls.get_name(ii) )
        page.insert_marks ( marks, grades, k_lst )
        page.insert_grades( marks, grades )
        page.commit()
    
        progress_bar.step()

#------------------------------------------------------------------------------#
