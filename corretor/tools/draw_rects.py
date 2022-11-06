#------------------------------------------------------------------------------#

import os
import sys
import fitz

sys.path.append('..')

from grading.tools    import pix_to_gray_image
from grading.page_ena import PageENA

#------------------------------------------------------------------------------#

example_dir = '../../docs/example/'
model_fname = example_dir + 'exemplo-modelo.pdf' if len(sys.argv) < 2 else sys.argv[1]
rects_fname = 'rects.pdf'                        if len(sys.argv) < 3 else sys.argv[2]

_DPI        = 300
_COLORSPACE = 'GRAY'

#------------------------------------------------------------------------------#

model_pdf = fitz.open(model_fname)
rects_pdf = fitz.open()

model_page = model_pdf[0]
model_pix  = model_page.get_pixmap( dpi=_DPI, colorspace=_COLORSPACE )
image      = pix_to_gray_image( model_pix )

page = PageENA( rects_pdf )

page.create_page()
page.insert_image( image )
page.draw_all_rects()

page.commit()

model_pdf.close()
rects_pdf.save(rects_fname)

#------------------------------------------------------------------------------#
