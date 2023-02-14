#------------------------------------------------------------------------------#
'''Test script that grades one page'''

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import fitz
import argparse

import grading.rectangles as rects

from grading.image_manip import ImageManipulation
from grading.answers     import Answers
from grading.marks       import collect_marks
from grading.ena_form    import ENAForm

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('model',   help='PDF file with the answers page model')
    parser.add_argument('keys',    help='TXT file with the answers keys')
    parser.add_argument('answers', help='PDF file with the answers')
    parser.add_argument('output',  help='Output file')
    parser.add_argument('-p', '--page', help='Page number to be graded', type=int, default=0)
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    model_pdf       = fitz.open(args.model)
    answers_pdf     = fitz.open(args.answers)
    annotations_pdf = fitz.open()

    with open( args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    answers = Answers(keys)

    #------------------------------------------------------------------------------#

    model_page   = model_pdf[0]
    model_pixmap = model_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')

    imag_manip = ImageManipulation()
    imag_manip.set_model(model_pixmap)

    original_page   = answers_pdf[args.page]
    original_pixmap = original_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')

    imag_manip.register_image(original_pixmap)
    eliminated, absent, marks = collect_marks(imag_manip.get_binary())
    answers.check_answers(eliminated, absent, marks)

    page = annotations_pdf.new_page(
        width  = rects.PAGE.width,
        height = rects.PAGE.height
    )

    form = ENAForm(page)
    form.insert_image(imag_manip.get_jpg())
    form.insert_name('TEST', imag_manip.bg_gray())
    form.insert_grades(answers)
    form.commit()

    model_pdf.close()
    answers_pdf.close()
    annotations_pdf.save(args.output)

#------------------------------------------------------------------------------#
