#------------------------------------------------------------------------------#
'''Test script that grades one page'''

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import argparse

from grading.image_manip import ImageManipulation
from grading.answers     import Answers
from grading.ena_form    import ENAForm
from grading.pdfs        import InputPDF, OutputPDF

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('model',  help='PDF file with the answers page model')
    parser.add_argument('keys',   help='TXT file with the answers keys')
    parser.add_argument('exam',   help='PDF file with the answers')
    parser.add_argument('output', help='Output file')
    parser.add_argument('-p', '--page', help='Page number to be graded', type=int, default=0)
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    model  = InputPDF(args.model)
    exam   = InputPDF(args.exam)
    output = OutputPDF()

    with open( args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    #------------------------------------------------------------------------------#

    answers = Answers(keys, 15)

    model_pixmap = model.get_pixmap(0)

    imag_manip = ImageManipulation()
    imag_manip.set_model(model_pixmap)

    exam_pixmap = exam.get_pixmap(args.page)

    imag_manip.register_image(exam_pixmap)

    answers.check_answers(imag_manip.get_binary())

    page = output.new_page()

    form = ENAForm(page)
    form.insert_image (imag_manip.get_jpg())
    form.insert_name  ('TEST', imag_manip.bg_gray())
    form.insert_grades(answers)
    form.commit()

    output.save(args.output)

    model .close()
    exam  .close()
    output.close()

#------------------------------------------------------------------------------#
