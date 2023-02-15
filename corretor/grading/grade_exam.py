#------------------------------------------------------------------------------#
'''Create the function grade_exam'''

import fitz

import grading.rectangles as rects

from grading.answers     import Answers
from grading.ena_form    import ENAForm
from grading.image_manip import ImageManipulation
from grading.xls_grades  import XLSGrades

#------------------------------------------------------------------------------#
def grade_exam(
    model_pdf:       fitz.Document,
    keys:            str,
    answers_pdf:     fitz.Document,
    annotations_pdf: fitz.Document,
    grades_xls:      XLSGrades,
    progress
) -> bool:

    model_page   = model_pdf[0]
    model_pixmap = model_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')

    imag_manip = ImageManipulation()
    imag_manip.set_model(model_pixmap)

    answers = Answers(keys)

    progress.start(answers_pdf.page_count)

    for ii, original_page in enumerate(answers_pdf):

        pixmap = original_page.get_pixmap(dpi=rects.DPI, colorspace='GRAY')

        imag_manip.register_image(pixmap)

        answers.check_answers(imag_manip.get_binary())

        grades_xls.add_grade(ii, answers)

        page = annotations_pdf.new_page(
            width  = rects.PAGE.width,
            height = rects.PAGE.height
        )

        form = ENAForm(page)
        form.insert_image (imag_manip.get_jpg())
        form.insert_name  (grades_xls.get_name(ii), imag_manip.bg_gray())
        form.insert_marks (answers)
        form.insert_grades(answers)
        form.commit()

        # Stop if process was canceled by user
        if not progress.step():
            return False

    return True

#------------------------------------------------------------------------------#
