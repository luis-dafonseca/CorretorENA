#------------------------------------------------------------------------------#

import os
import sys
import fitz

sys.path.append('..')

import grading.ena_param     as ep
from   grading.answers_key   import AnswersKey
from   grading.tools         import pix_to_gray_image
from   grading.registration  import Registration
from   grading.collect_marks import collect_marks
from   grading.page_ena      import PageENA

#------------------------------------------------------------------------------#

example_dir = '../../docs/example/'

model_name       = example_dir + 'exemplo-modelo.pdf'
answers_name     = example_dir + 'exemplo-respostas.pdf'
annotations_name = 'grading.pdf'

n_page = 0 if len(sys.argv) < 2 else int(sys.argv[1])-1

#------------------------------------------------------------------------------#

model_pdf       = fitz.open(model_name)
answers_pdf     = fitz.open(answers_name)
annotations_pdf = fitz.open()

#                         1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
answers_key = AnswersKey('D E B B E A A X B D D C D B C C B E E B A A A E E B E B D D')

#------------------------------------------------------------------------------#

page  = model_pdf[0]
pix   = page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE )
image = pix_to_gray_image( pix )
reg   = Registration( image )

original_page = answers_pdf[n_page]
original_pix  = original_page.get_pixmap( dpi=ep.DPI, colorspace=ep.COLORSPACE ) 
original_img  = pix_to_gray_image( original_pix )

image  = reg.transform( original_img )
marks  = collect_marks( image )
grades = answers_key.check( marks )

page = PageENA( annotations_pdf )
page.create_page  ()
page.insert_image ( image )
page.insert_annul ( answers_key.keys )
page.insert_marks ( marks, grades, answers_key.keys )
page.insert_grades( grades )
page.commit()

model_pdf.close()
answers_pdf.close()
annotations_pdf.save(annotations_name)

#------------------------------------------------------------------------------#
