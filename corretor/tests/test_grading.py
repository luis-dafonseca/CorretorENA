#------------------------------------------------------------------------------#
"""
Test script that grades one page
"""

#------------------------------------------------------------------------------#

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import fitz
import argparse

import grading.rectangles as rects

from grading.answers      import Answers
from grading.tools        import pix_to_gray_image
from grading.registration import Registration
from grading.marks        import collect_marks
from grading.ena_form     import ENAForm

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

    model = model_pdf[0]
    pix   = model.get_pixmap(dpi=rects.DPI, colorspace='GRAY')
    image = pix_to_gray_image(pix)
    reg   = Registration(image)

    original_page = answers_pdf[args.page]
    original_pix  = original_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')
    original_img  = pix_to_gray_image(original_pix)

    image  = reg.transform(original_img)
    marks  = collect_marks(image)
    answers.check_answers(marks)

    page = annotations_pdf.new_page(
        width  = rects.PAGE.width,
        height = rects.PAGE.height
    )

    form = ENAForm(page)
    form.insert_image (image)
    form.insert_name('TESTE', 0.9)
    form.insert_grades(answers)
    form.commit()

    model_pdf.close()
    answers_pdf.close()
    annotations_pdf.save(args.output)

#------------------------------------------------------------------------------#
