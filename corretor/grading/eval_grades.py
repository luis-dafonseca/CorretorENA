#------------------------------------------------------------------------------#
'''Create the function grade_exam'''

from grading.pdfs         import InputPDF, OutputPDF
from grading.answers      import Answers
from grading.ena_form     import ENAForm
from grading.image_manip  import ImageManipulation
from grading.spreadsheets import ResultsSheet

#------------------------------------------------------------------------------#
def eval_grades(
    model:   InputPDF,
    keys:    str,
    exam:    InputPDF,
    annot:   OutputPDF,
    results: ResultsSheet,
    progress
) -> bool:

    model_pixmap = model.get_pixmap(0)

    imag_manip = ImageManipulation()
    imag_manip.set_model(model_pixmap)

    answers = Answers(keys)

    n_pages = exam.page_count

    progress.start(n_pages)

    for ii in range(n_pages):

        pixmap = exam.get_pixmap(ii)

        imag_manip.register_image(pixmap)

        answers.check_answers(imag_manip.get_binary())

        results.add_grade(ii, answers)
        name = results.get_name(ii)

        page = annot.new_page()

        form = ENAForm(page)
        form.insert_image (imag_manip.get_jpg())
        form.insert_name  (name, imag_manip.bg_gray())
        form.insert_marks (answers)
        form.insert_grades(answers)
        form.commit()

        # Stop if process was canceled by user
        if not progress.step():
            return False

    return True

#------------------------------------------------------------------------------#
