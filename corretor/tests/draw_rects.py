#------------------------------------------------------------------------------#

"""
Test script that reads a model and draw all rectangles on it.
"""

#------------------------------------------------------------------------------#

import sys
import fitz
import argparse

sys.path.append('..')

import ena_param as ep

from grading.tools    import pix_to_gray_image
from grading.page_ena import PageENA

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( 'model',  help='PDF file with the answers page model' )
    parser.add_argument( 'output', help='Output file' )
    args = parser.parse_args()
    
    #--------------------------------------------------------------------------#
    
    mod_pdf = fitz.open(args.model)
    out_pdf = fitz.open()

    model_page = mod_pdf[0]
    model_pix  = model_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )
    image      = pix_to_gray_image( model_pix )
    
    page = PageENA( out_pdf )
    
    page.create_page()
    page.insert_image(image)
    page.draw_all_rects()
    
    page.commit()
    
    mod_pdf.close()
    out_pdf.save(args.output)

#------------------------------------------------------------------------------#
