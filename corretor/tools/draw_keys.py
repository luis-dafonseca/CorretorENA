#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
import sys
import fitz

sys.path.append('..')

from grading.tools       import pix_to_gray_image
from grading.page_ena    import PageENA
from grading.answers_key import AnswersKey

#------------------------------------------------------------------------------#

model_fname = "../../../pdf/modelo.pdf" if len(sys.argv) < 2 else sys.argv[1]
rects_fname = 'keys.pdf'                if len(sys.argv) < 3 else sys.argv[2]

_DPI        = 300
_COLORSPACE = "GRAY"

#------------------------------------------------------------------------------#

model_pdf = fitz.open(model_fname)
rects_pdf = fitz.open()

answers_key = AnswersKey('C B E A C B E D C B E E A D C C D B A D A D A C D E A E B D') # 2023

model_page = model_pdf.load_page(0)
model_pix  = model_page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE )
image      = pix_to_gray_image( model_pix )

page = PageENA( rects_pdf )

page.create_page()
page.insert_image( image )
page.draw_answers_key( answers_key.keys )

page.commit()

model_pdf.close()
rects_pdf.save(rects_fname)

#------------------------------------------------------------------------------#
