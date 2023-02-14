#------------------------------------------------------------------------------#
"""
Test script to draw keys to a model PDF file
"""

#------------------------------------------------------------------------------#

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import argparse
import fitz

import grading.rectangles as rects
from grading.ena_form import ENAForm

#-----------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('model',  help='PDF file with the answers page model')
    parser.add_argument('keys',   help='TXT file with the answers keys')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    with open(args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    mod_pdf = fitz.open(args.model)
    out_pdf = fitz.open()

    model_page   = mod_pdf[0]
    model_pixmap = model_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')

    page = out_pdf.new_page(
        width  = rects.PAGE.width,
        height = rects.PAGE.height
    )

    form = ENAForm(page)
    form.insert_pixmap(model_pixmap)
    form.insert_keys  (keys)
    form.commit()

    mod_pdf.close()
    out_pdf.save(args.output)

#------------------------------------------------------------------------------#
