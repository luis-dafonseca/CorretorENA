#------------------------------------------------------------------------------#

"""
Test script that grades one page.
"""

#------------------------------------------------------------------------------#

import sys
import fitz
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import ena_param as ep

from grading.grades       import check_answers, keys_str_to_list
from grading.tools        import pix_to_gray_image
from grading.registration import Registration
from grading.marks        import collect_marks
from grading.page_ena     import PageENA

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( 'model',   help='PDF file with the answers page model' )
    parser.add_argument( 'keys',    help='TXT file with the answers keys' )
    parser.add_argument( 'answers', help='PDF file with the answers' )
    parser.add_argument( 'output',  help='Output file' )
    parser.add_argument( '-p', '--page', help='Page number to be graded', type=int, default=0 )
    args = parser.parse_args()
    
    #--------------------------------------------------------------------------#
    
    model_pdf       = fitz.open(args.model)
    answers_pdf     = fitz.open(args.answers)
    annotations_pdf = fitz.open()

    with open( args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    k_lst = keys_str_to_list( keys )
    
    #------------------------------------------------------------------------------#
    
    page  = model_pdf[0]
    pix   = page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )
    image = pix_to_gray_image( pix )
    reg   = Registration( image )
    
    original_page = answers_pdf[args.page]
    original_pix  = original_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE ) 
    original_img  = pix_to_gray_image( original_pix )
    
    image  = reg.transform( original_img )
    marks  = collect_marks( image )
    grades = check_answers( marks, k_lst )
    
    page = PageENA( annotations_pdf )
    page.create_page  ()
    page.insert_image ( image )
    page.insert_marks ( marks, grades, k_lst )
    page.insert_grades( marks, grades )
    page.commit()
    
    model_pdf.close()
    answers_pdf.close()
    annotations_pdf.save(args.output)

#------------------------------------------------------------------------------#
