#------------------------------------------------------------------------------#

"""
Test script that reads a model and the answers keys to draw the answers on the mark positions.
"""

#------------------------------------------------------------------------------#

import sys
import fitz
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import ena_param as ep

from grading.tools    import pix_to_gray_image
from grading.page_ena import PageENA
from grading.grades   import keys_str_to_list

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( 'model',  help='PDF file with the answers page model' )
    parser.add_argument( 'keys',   help='TXT file with the answers keys' )
    parser.add_argument( 'output', help='Output file' )
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    mod_pdf = fitz.open(args.model)
    out_pdf = fitz.open()

    with open( args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    k_lst = keys_str_to_list( keys )

    model_page = mod_pdf[0]
    model_pix  = model_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )
    image      = pix_to_gray_image( model_pix )

    page = PageENA( out_pdf )

    page.create_page()
    page.insert_image(image)
    page.draw_answers_key(k_lst)

    page.commit()

    mod_pdf.close()
    out_pdf.save(args.output)

#------------------------------------------------------------------------------#
