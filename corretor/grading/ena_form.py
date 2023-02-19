#------------------------------------------------------------------------------#
'''Define class ENAForm to draw annotations to PDF pages'''

import io
import fitz

import grading.rectangles as rects

from grading.answers import Answers, keys_str_to_list
from grading.pdfs    import InputPDF, OutputPDF

COLOR_CORRECT       = (0,0,1)
COLOR_INCORRECT     = (1,0,0)
COLOR_MASK          = (1,0,1)
COLOR_ANNUL         = (0,0,1)
COLOR_ENTRY         = (0,0,1)
COLOR_SCORE         = (1,0,0)
COLOR_ANSWER        = (0,0,1)
COLOR_KEY           = (0,0,1)
COLOR_KEY_INCORRECT = (0,0.7,0.7)
COLOR_NAME          = (0,0,1)

# ------------------------------------------------------------------------------#
def create_keys_page(model: InputPDF, output:OutputPDF, keys: str) -> None:
    '''Extract input first page add it to output and draw answer keys'''

    form = ENAForm(output.new_page())

    form.insert_pixmap(model.get_pixmap(0))

    form.insert_name('GABARITO', 1)
    form.insert_keys(keys)

    form.commit()

# ------------------------------------------------------------------------------#
def create_fields_page(
    model:  InputPDF,
    output: OutputPDF,
    extra:  bool = False
) -> None:
    '''Extract input first page add it to output and draw rectangles'''

    form = ENAForm(output.new_page())

    form.insert_pixmap(model.get_pixmap(0))

    form.insert_name('CAMPOS', 1)

    if extra:
        form.insert_extra_rects()

    form.insert_rects()

    form.commit()

# ------------------------------------------------------------------------------#
class ENAForm:
    '''Draw annotations to PDF page'''

    # --------------------------------------------------------------------------#
    def __init__(self, page: fitz.Page) -> None:
        '''Create an ENA Form for a PDF page'''

        self.page = page
        self.shape: fitz.Shape = page.new_shape()

    # --------------------------------------------------------------------------#
    def commit(self) -> None:
        ''' Commit changes to PDF page.
        This function must be called after changes are made.
        '''
        self.shape.commit()

    # --------------------------------------------------------------------------#
    def insert_pixmap(self, pixmap: fitz.Pixmap) -> None:
        '''Insert a pixmap image as page background'''

        self.page.insert_image(rects.PAGE, pixmap=pixmap)

    # --------------------------------------------------------------------------#
    def insert_image(self, image_buffer) -> None:
        '''Insert an image as page background'''

        self.page.insert_image(rects.PAGE, stream=io.BytesIO(image_buffer))

    # --------------------------------------------------------------------------#
    def insert_name(self, name: str, bg_gray: float = 1) -> None:
        '''Write candidate name to page'''

        bg_color = (bg_gray, bg_gray, bg_gray)

        self.shape.draw_rect(rects.NAME)
        self.shape.finish(
            color = bg_color,
            fill  = bg_color
        )

        self.shape.insert_textbox(
            rects.NAME_TEXT,
            name,
            color    = COLOR_NAME,
            fontsize = int(0.9*rects.NAME_TEXT.height),
            align    = fitz.TEXT_ALIGN_LEFT
        )
        self.shape.finish()

    #--------------------------------------------------------------------------#
    def insert_grades(self, answers: Answers) -> None:
        '''Write candidate scores and draw marks to page'''

        self.insert_scores(answers)
        self.insert_marks (answers)

    #--------------------------------------------------------------------------#
    def insert_scores(self, answers: Answers) -> None:
        '''Write candidate scores to page'''

        #----------------------------------------------------------------------#
        def write_final_score(shape, text: str, color: tuple[int]) -> None:
            '''Convenience function to write on final grade field'''

            font_size = int( 0.9*rects.FINAL_GRADE.height )

            shape.insert_textbox(
                rects.FINAL_GRADE,
                text,
                color=color,
                fontsize=font_size,
                align=fitz.TEXT_ALIGN_LEFT
            )
            shape.finish()
        #----------------------------------------------------------------------#

        # Write if candidate was eliminated of absent and exit function
        if answers.eliminated or answers.absent:
            text = 'Eliminado' if answers.eliminated else 'Ausente'
            write_final_score( self.shape, text, COLOR_INCORRECT)
            return

        # Write the score for each answer
        font_size = int(0.9*rects.GRADE_TEXT[0].height)

        for ii in range(rects.N_QUESTIONS):

            correct = answers.correct[ii]
            color   = COLOR_CORRECT if correct else COLOR_INCORRECT

            self.shape.insert_textbox(
                rects.GRADE_TEXT[ii],
                str(correct),
                color=color,
                fontsize=font_size,
                align=fitz.TEXT_ALIGN_CENTER
            )

        # Write the final score
        total = answers.total
        text  = f'{total:3}'
        color = COLOR_CORRECT if answers.approved else COLOR_INCORRECT
        write_final_score(self.shape, text, color)

    #--------------------------------------------------------------------------#
    def insert_marks(self, answers: Answers) -> None:
        '''Draw candidate marks on PDF page'''

        # Mark if candidate was eliminated or absent and exit function
        if answers.eliminated or answers.absent:
            rect = rects.ELIMINATED if answers.eliminated else rects.ABSENT
            self.shape.draw_rect(rect)
            self.shape.finish(width=10, color=COLOR_INCORRECT)
            return

        self.draw_correct_answers     (answers)
        self.draw_wrong_answers       (answers)
        self.draw_key_on_wrong_answers(answers)
        self.draw_annulated_questions (answers.keys)

    #--------------------------------------------------------------------------#
    def insert_keys(self, keys: list[int] | str) -> None:
        '''Draw keys to page'''

        keys = keys_str_to_list(keys)

        self.draw_annulated_questions(keys)

        for ii, jj in [ (ii,jj) for ii, jj in enumerate(keys) if jj != -1 ]:
            self.shape.draw_rect(rects.MARK[ii][jj])

        self.shape.finish(
            width = 2,
            color = (0, 0, 0),
            fill  = COLOR_KEY,
            fill_opacity=0.5
        )

    #--------------------------------------------------------------------------#
    def insert_rects(self) -> None:
        '''Draw main rectangles to page'''

        # Score entries
        for ii in range(rects.N_QUESTIONS):
            self.shape.draw_rect(rects.GRADE[ii])
        self.shape.finish(width=5, color=COLOR_SCORE)

        # Answer entries
        for ii in range(rects.N_QUESTIONS):
            for jj in range(5):
                self.shape.draw_rect(rects.MARK[ii][jj])
        self.shape.finish(width=5, color=COLOR_ANSWER)

        # Absent and eliminated
        self.shape.draw_rect(rects.ABSENT)
        self.shape.draw_rect(rects.ELIMINATED)
        self.shape.finish(width=5, color=COLOR_ENTRY)


    #--------------------------------------------------------------------------#
    def insert_extra_rects(self) -> None:
        '''Draw extra rectangles to page'''

        # Mask
        self.shape.draw_rect(rects.REGISTRATION_MASK)
        self.shape.finish(width=5, color=COLOR_MASK, dashes='[20] 0')

        # Name
        self.shape.draw_rect(rects.NAME)
        self.shape.finish(width=5, color=COLOR_ENTRY)

        # Answers and Scores box
        self.shape.draw_rect(rects.MARKS_BOX_LEFT  )
        self.shape.draw_rect(rects.MARKS_BOX_RIGHT )
        self.shape.draw_rect(rects.GRADES_BOX_LEFT )
        self.shape.draw_rect(rects.GRADES_BOX_RIGHT)

        # Background sampling
        self.shape.draw_rect(rects.BACKGROUND)
        self.shape.draw_rect(rects.BACKGROUND_GRAY)

        self.shape.finish(
            width = 1,
            color = COLOR_MASK,
            fill  = COLOR_MASK,
            fill_opacity = 0.05
        )

        self.shape.draw_rect(rects.FINAL_GRADE)
        self.shape.finish(width=5, color=COLOR_SCORE)

    #--------------------------------------------------------------------------#
    # Raw drawing functions
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def draw_correct_answers(self, answers: Answers) -> None:
        '''Draw correct answers'''

        for ii in [ ii for ii, cc in enumerate(answers.correct) if cc ]:
            key = answers.keys[ii]
            if key != -1:
                self.shape.draw_rect(rects.MARK[ii][key])

        self.shape.finish(
            width = 7,
            color = COLOR_CORRECT
        )

    #--------------------------------------------------------------------------#
    def draw_wrong_answers(self, answers: Answers) -> None:
        '''Draw wrong answers'''

        for ii, ans in enumerate(answers.answers):
            if answers.correct[ii]:
                continue
            for jj in ans:
                self.shape.draw_rect(rects.MARK[ii][jj])

        self.shape.finish(
            width = 7,
            color = COLOR_INCORRECT
        )

    #--------------------------------------------------------------------------#
    def draw_key_on_wrong_answers(self, answers: Answers) -> None:
        '''Draw key on wrong answers'''

        for ii in [ ii for ii, cc in enumerate(answers.correct) if not cc ]:
            self.shape.draw_rect(rects.MARK[ii][answers.keys[ii]])

        self.shape.finish(
            width = 1,
            color = COLOR_KEY_INCORRECT,
            fill  = COLOR_KEY_INCORRECT,
            fill_opacity = 0.4
        )

    #--------------------------------------------------------------------------#
    def draw_annulated_questions(self, keys: list[int]) -> None:

        #----------------------------------------------------------------------#
        def draw_annul(shape, ii:int) -> None:

            r1 = rects.MARK[ii][0]
            r2 = rects.MARK[ii][4]

            p1 = [ r1.x0+5, (r1.y0+r1.y1)/2 ]
            p2 = [ r2.x1-5, (r2.y0+r2.y1)/2 ]

            bb = r1.height / 5

            shape.draw_squiggle(p1, p2, breadth=bb)
        #----------------------------------------------------------------------#

        for ii in [ ii for ii, kk in enumerate(keys) if kk == -1 ]:
            draw_annul(self.shape, ii)

        self.shape.finish(
            width=5,
            color=COLOR_ANNUL,
            closePath=False
        )

#------------------------------------------------------------------------------#
