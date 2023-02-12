#------------------------------------------------------------------------------#

import fitz
import cv2
import io

import ena_param          as ep
import grading.rectangles as rects

from grading.grades import Grades

COLOR_NAME_BG   = (1,1,1)
COLOR_CORRECT   = (0,0,1)
COLOR_INCORRECT = (1,0,0)
COLOR_MASK      = (1,0,1)
COLOR_ANNUL     = (1,0,1)
COLOR_ENTRY     = (0,0,1)
COLOR_SCORE     = (1,0,0)
COLOR_ANSWER    = (0,0,1)
COLOR_ENTRY     = (0,0,1)
COLOR_KEY       = (0,0,1)

# ------------------------------------------------------------------------------#

class PageENA:

    # --------------------------------------------------------------------------#
    def __init__(self, pdf_doc):

        self.doc = pdf_doc

    # --------------------------------------------------------------------------#
    def get_page(self, page_number=0):

        self.page  = self.doc[page_number]
        self.shape = self.page.new_shape()

    # --------------------------------------------------------------------------#
    def create_page(self):

        self.page = self.doc.new_page(
            width  = rects.PAGE.width,
            height = rects.PAGE.height
        )
        self.shape = self.page.new_shape()

    # --------------------------------------------------------------------------#
    def insert_pixmap(self, pixmap_):

        self.page.insert_image(rects.PAGE, pixmap=pixmap_)

    # --------------------------------------------------------------------------#
    def insert_image(self, image):

        is_success, buffer = cv2.imencode('.jpg', image)

        self.page.insert_image(rects.PAGE, stream=io.BytesIO(buffer))

    # --------------------------------------------------------------------------#
    def commit(self):
        self.shape.commit()

    # --------------------------------------------------------------------------#
    def insert_name(self, name: str):

        self.shape.draw_rect(rects.NAME)
        self.shape.finish(color=COLOR_NAME_BG, fill=COLOR_NAME_BG)

        self.shape.insert_textbox(
            rects.NAME_TEXT,
            name,
            color    = COLOR_CORRECT,
            fontsize = int(0.8*rects.NAME_TEXT.height),
            align    = fitz.TEXT_ALIGN_LEFT
        )
        self.shape.finish()

    #--------------------------------------------------------------------------#
    def insert_grades(self, marks, grades: Grades):

        final_font  = int( 0.9*rects.FINAL_GRADE.height )
        final_color = COLOR_INCORRECT

        if marks.eliminated:
            self.shape.insert_textbox(
                rects.FINAL_GRADE,
                'Eliminado',
                color=final_color,
                fontsize=final_font,
                align=fitz.TEXT_ALIGN_LEFT
            )
            self.shape.finish()
            return

        if marks.absent:
            self.shape.insert_textbox(
                rects.FINAL_GRADE,
                'Ausente',
                color=final_color,
                fontsize=final_font,
                align=fitz.TEXT_ALIGN_LEFT
            )
            self.shape.finish()
            return

        for ii in range(ep.N_QUESTIONS):

            nn = grades.question[ii]
            cc = COLOR_CORRECT if nn else COLOR_INCORRECT

            self.shape.insert_textbox(
                rects.GRADE_TEXT[ii],
                str(nn),
                color=cc,
                fontsize=int(0.9*rects.GRADE_TEXT[ii].height),
                align=fitz.TEXT_ALIGN_CENTER
            )

        tt = grades.total
        final_color = COLOR_CORRECT if tt >= ep.MIN_SCORE else COLOR_INCORRECT

        self.shape.insert_textbox(
            rects.FINAL_GRADE,
            f'{tt:3}',
            color=final_color,
            fontsize=final_font,
            align=fitz.TEXT_ALIGN_LEFT
        )
        self.shape.finish()

    #--------------------------------------------------------------------------#
    def insert_marks( self, marks, grades: Grades, k_lst ):

        if marks.eliminated:
            self.shape.draw_rect( rects.ELIMINATED )
            self.shape.finish( width=10, color=COLOR_INCORRECT )
            return

        if marks.absent:
            self.shape.draw_rect( rects.ABSENT )
            self.shape.finish( width=10, color=COLOR_INCORRECT )
            return

        # Draw the correct answer on wrong marks
        for ii in [ ii for ii, nn in enumerate(grades.question) if nn == 0 ]:
            self._draw_key( ii, k_lst[ii] )
        self.shape.finish( width=1, color=COLOR_KEY, fill=COLOR_KEY, fill_opacity=0.2 )

        # Draw correct answers
        for ii in [ ii for ii, nn in enumerate(grades.question) if nn == 1 and k_lst[ii] != -1 ]:
            jj = marks.question[ii][0]
            self.shape.draw_rect( rects.MARK[ii][jj] )
        self.shape.finish( width=7, color=COLOR_CORRECT )

        # Draw wrong answers
        for ii in [ ii for ii, nn in enumerate(grades.question) if nn == 0 ]:
            for jj in marks.question[ii]:
                self.shape.draw_rect( rects.MARK[ii][jj] )
        self.shape.finish( width=7, color=COLOR_INCORRECT )

        # Draw canceled questions
        self._insert_annul( k_lst )

    #--------------------------------------------------------------------------#
    def _draw_annul( self, ii ):

        r1 = rects.MARK[ii][0]
        r2 = rects.MARK[ii][4]

        p1 = [ r1.x0+5, (r1.y0+r1.y1)/2 ]
        p2 = [ r2.x1-5, (r2.y0+r2.y1)/2 ]

        bb = r1.height/5

        self.shape.draw_squiggle(p1, p2, breadth=bb)

    #--------------------------------------------------------------------------#
    def _insert_annul( self, keys ):

        for ii in [ ii for ii, nn in enumerate(keys) if nn == -1 ]:
            self._draw_annul(ii)
        self.shape.finish( width=5, color=COLOR_ANNUL, closePath=False)

    #--------------------------------------------------------------------------#
    def draw_all_rects(self):

        # Mask
        self.shape.draw_rect( rects.REGISTRATION_MASK )
        self.shape.finish( width=5, color=COLOR_MASK, dashes='[20] 0' )

        # Name
        self.shape.draw_rect( rects.NAME )
        self.shape.finish( width=5, color=COLOR_ENTRY )

        # Answers box
        self.shape.draw_rect( rects.MARKS_BOX_LEFT  )
        self.shape.draw_rect( rects.MARKS_BOX_RIGHT )
        self.shape.finish( width=5, color=COLOR_MASK )

        # Scores box
        self.shape.draw_rect( rects.GRADES_BOX_LEFT  )
        self.shape.draw_rect( rects.GRADES_BOX_RIGHT )
        self.shape.finish( width=5, color=COLOR_MASK )

        # Score entries
        for ii in range(ep.N_QUESTIONS):
            self.shape.draw_rect( rects.GRADE[ii] )
        self.shape.draw_rect( rects.FINAL_GRADE )
        self.shape.finish( width=5, color=COLOR_SCORE )

        # Answer entries
        for ii in range(ep.N_QUESTIONS):
            for jj in range(5):
                self.shape.draw_rect( rects.MARK[ii][jj] )
        self.shape.finish( width=5, color=COLOR_ANSWER )

        # Absent and eliminated
        self.shape.draw_rect( rects.ABSENT     )
        self.shape.draw_rect( rects.ELIMINATED )
        self.shape.finish( width=5, color=COLOR_ENTRY )

    #--------------------------------------------------------------------------#
    def _draw_key( self, ii, jj ):
        self.shape.draw_rect( rects.MARK[ii][jj] )

    #--------------------------------------------------------------------------#
    def draw_answers_key( self, keys ):

        self._insert_annul( keys )

        for ii, jj in [ (ii,jj) for ii, jj in enumerate(keys) if jj != -1 ]:
            self._draw_key( ii, jj )

        self.shape.finish(
            width=2,
            color=(0, 0, 0),
            fill=COLOR_KEY,
            fill_opacity=0.5
        )

#------------------------------------------------------------------------------#
