#------------------------------------------------------------------------------#

import fitz

import ena_param as ep
import grading.rectangles as rects

from grading.answers      import Answers
from grading.ena_form     import ENAForm
from grading.marks        import collect_marks
from grading.registration import Registration
from grading.tools        import pix_to_gray_image


#------------------------------------------------------------------------------#
def create_model_registration(model_pdf):

    page = model_pdf[0]

    pix = page.get_pixmap(
        dpi=rects.DPI,
        colorspace='GRAY'
    )

    image = pix_to_gray_image(pix)

    return Registration(image)

#------------------------------------------------------------------------------#
def grade_exam(model_pdf: fitz.Document,
               keys: str,
               answers_pdf: fitz.Document,
               annotations_pdf: fitz.Document,
               grades_xls,
               progress ) -> bool:

    reg = create_model_registration(model_pdf)

    answers = Answers(keys)

    progress.start(answers_pdf.page_count)

    for ii, original_page in enumerate(answers_pdf):

        original_pix = original_page.get_pixmap(
            dpi        = rects.DPI,
            colorspace ='GRAY'
            )
        original_img = pix_to_gray_image(original_pix)

        image = reg.transform(original_img)
        marks = collect_marks(image)
        answers.check_answers(marks)

        grades_xls.add_grade(
            ii,
            answers.eliminated,
            answers.absent,
            answers.total
        )

        page = annotations_pdf.new_page(
            width  = rects.PAGE.width,
            height = rects.PAGE.height
        )

        form = ENAForm(page)
        form.insert_image (image)
        form.insert_name  (grades_xls.get_name(ii))
        form.insert_marks (answers)
        form.insert_grades(answers)
        form.commit()

        # Stop if process was canceled by user
        if not progress.step():
            return False

    return True

#------------------------------------------------------------------------------#
