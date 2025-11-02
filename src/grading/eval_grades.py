#------------------------------------------------------------------------------#
'''Create the function grade_exam'''

from typing import Protocol

from grading.pdfs         import InputPDF, OutputPDF
from grading.answers      import Answers
from grading.ena_form     import ENAForm
from grading.image_manip  import ImageManipulation
from grading.spreadsheets import ResultsSheet

#------------------------------------------------------------------------------#
class ProgressBar(Protocol):
    '''Protocol class to specify the progress bar interface'''

    def start(self, total_of_steps: int) -> None:
        '''Start the progress bar providing the number of steps'''

    def step(self) -> bool:
        '''Add one step to progress bar

        Return:
            False if user asked to interrupt the process
        '''

#------------------------------------------------------------------------------#
def eval_grades(
    model:   InputPDF,
    keys:    str,
    minimum: int,
    exam:    InputPDF,
    annot:   OutputPDF,
    results: ResultsSheet,
    progress
) -> bool:

    model_pixmap = model.get_pixmap(0)

    imag_manip = ImageManipulation()
    imag_manip.set_model(model_pixmap)

    answers = Answers(keys, minimum)

    n_pages = exam.page_count()

    progress.start(n_pages)

    for ii in range(n_pages):

        imag_manip.register_image(exam.get_pixmap(ii))

        answers.check_answers(imag_manip.get_binary())

        results.add_grade(ii, answers)
        name = results.get_name(ii)

        form = ENAForm(annot.new_page())
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
