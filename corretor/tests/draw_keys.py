#------------------------------------------------------------------------------#

import os
import sys
import fitz

sys.path.append('..')

import grading.ena_param as ep
from   grading.tools     import pix_to_gray_image
from   grading.page_ena  import PageENA
from   grading.grades    import keys_str_to_list

#------------------------------------------------------------------------------#

example_dir = '../../docs/example/'
model_fname = example_dir + 'exemplo-modelo.pdf' if len(sys.argv) < 2 else sys.argv[1]
keys_fname  = 'keys.pdf'                         if len(sys.argv) < 3 else sys.argv[2]

#------------------------------------------------------------------------------#

model_pdf = fitz.open(model_fname)
keys_pdf  = fitz.open()

keys = 'CBEACBEDCXEEADCCDXADADACDEAEBD'
k_lst = keys_str_to_list( keys )

model_page = model_pdf[0]
model_pix  = model_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )
image      = pix_to_gray_image( model_pix )

page = PageENA( keys_pdf )

page.create_page()
page.insert_image( image )
page.draw_answers_key( k_lst )

page.commit()

model_pdf.close()
keys_pdf.save(keys_fname)

#------------------------------------------------------------------------------#
