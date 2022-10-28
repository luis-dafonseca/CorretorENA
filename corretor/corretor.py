#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
import sys
import fitz

from grade_exam  import grade_exam
from answers_key import AnswersKey

#------------------------------------------------------------------------------#

pdf_dir = "../../pdf/"

fname = pdf_dir + "small.pdf" if len(sys.argv) < 2 else sys.argv[1]

name = os.path.basename(fname)
name = os.path.splitext(name)[0]

model_name       = pdf_dir + "modelo.pdf"
answers_name     = fname
annotations_name = f'{name}-anotacoes.pdf'
grades_name      = f'{name}-notas.xls'

#------------------------------------------------------------------------------#

model_pdf       = fitz.open(model_name)
answers_pdf     = fitz.open(answers_name)
annotations_pdf = fitz.open()
grades_xls      = None

answers_key = AnswersKey('d e b b e a a e b b d c d b c c b e e b a a a e e b e b d d')

grade_exam( model_pdf, answers_key, answers_pdf, annotations_pdf, grades_xls )

model_pdf.close()
answers_pdf.close()
annotations_pdf.save(annotations_name)
# close grades_xls

#------------------------------------------------------------------------------#
