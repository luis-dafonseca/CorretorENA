#------------------------------------------------------------------------------#

import os
import sys
import fitz

sys.path.append('..')

import grading.ena_param   as ep
from   grading.tools       import pix_to_gray_image
from   grading.page_ena    import PageENA
from   grading.answers_key import AnswersKey

#------------------------------------------------------------------------------#

example_dir = '../../docs/example/'
model_fname = example_dir + 'exemplo-modelo.pdf' if len(sys.argv) < 2 else sys.argv[1]
rects_fname = 'keys.pdf'                         if len(sys.argv) < 3 else sys.argv[2]

#------------------------------------------------------------------------------#

model_pdf = fitz.open(model_fname)
rects_pdf = fitz.open()

answers_key = AnswersKey('C B E A C B E D C X E E A D C C D X A D A D A C D E A E B D')

model_page = model_pdf[0]
model_pix  = model_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )
image      = pix_to_gray_image( model_pix )

page = PageENA( rects_pdf )

page.create_page()
page.insert_image( image )
page.draw_answers_key( answers_key.keys )

page.commit()

model_pdf.close()
rects_pdf.save(rects_fname)

#------------------------------------------------------------------------------#
