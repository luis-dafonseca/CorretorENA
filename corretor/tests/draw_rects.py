#------------------------------------------------------------------------------#

"""
Test script that reads a model and draw all rectangles on it
"""

#------------------------------------------------------------------------------#

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import argparse
import fitz

import grading.rectangles as rects

from grading.ena_form import ENAForm
from grading.tools    import pix_to_gray_image

#-----------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('model',  help='PDF file with the answers page model')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    mod_pdf = fitz.open(args.model)
    out_pdf = fitz.open()

    model_page = mod_pdf[0]
    model_pix  = model_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')

    page = out_pdf.new_page(
        width  = rects.PAGE.width,
        height = rects.PAGE.height
    )

    form = ENAForm(page)
    form.insert_pixmap(model_pix)
    form.insert_rects ()
    form.commit()

    mod_pdf.close()
    out_pdf.save(args.output)

#------------------------------------------------------------------------------#
