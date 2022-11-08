#------------------------------------------------------------------------------#

import fitz
import cv2
import io
import numpy as np

import grading.ena_param as ep
from   grading.rects import Rects

COLOR_NAME_BG   = (1,1,1)
COLOR_CORRECT   = (0,0,1)
COLOR_INCORRECT = (1,0,0)
COLOR_MASK      = (1,0,1)
COLOR_ANNUL     = (1,0,1)
COLOR_ENTRY     = (0,0,1)
COLOR_SCORE     = (1,0,0)
COLOR_ANSWER    = (0,0,1)
COLOR_ENTRY     = (0,0,1)
COLOR_KEY       = (1,0,1)

#------------------------------------------------------------------------------#
class PageENA:

    #--------------------------------------------------------------------------#
    def __init__( self, pdf_doc):

        self.doc = pdf_doc
        self.page_rect = Rects.full_page()

    #--------------------------------------------------------------------------#
    def get_page( self, page_number=0 ):

        self.page  = self.doc[page_number]
        self.shape = self.page.new_shape()

    #--------------------------------------------------------------------------#
    def create_page(self):

        self.page  = self.doc.new_page( width =self.page_rect.width, 
                                        height=self.page_rect.height )
        self.shape = self.page.new_shape()

    #--------------------------------------------------------------------------#
    def insert_image( self, image ):

        is_success, buffer = cv2.imencode( '.png', image )

        self.page.insert_image( self.page_rect, stream=io.BytesIO(buffer) )

    #--------------------------------------------------------------------------#
    def commit( self ):
        self.shape.commit()

    #--------------------------------------------------------------------------#
    def insert_name( self, name ):
    
        rr = Rects.name()
        self.shape.draw_rect( rr )
        self.shape.finish( color=COLOR_NAME_BG, fill=COLOR_NAME_BG ) 
        
        rr.y0 = (rr.y0 + rr.y1 ) // 2

        self.shape.insert_textbox( rr, name, color=COLOR_CORRECT,
                                   fontsize=int( 0.8*rr.height ),
                                   align=fitz.TEXT_ALIGN_LEFT )
        self.shape.finish() 

    #--------------------------------------------------------------------------#
    def insert_grades( self, marks, grades ):

        final_rect = Rects.full_grade()
        final_font = int( 0.9*final_rect.height )
        final_color = COLOR_INCORRECT

        if marks.eliminated:
            self.shape.insert_textbox( final_rect, 'Eliminado', 
                                       color    = final_color,
                                       fontsize = final_font,
                                       align    = fitz.TEXT_ALIGN_LEFT )
            self.shape.finish() 
            return

        if marks.absent:
            self.shape.insert_textbox( final_rect, 'Ausente', 
                                       color    = final_color,
                                       fontsize = final_font,
                                       align    = fitz.TEXT_ALIGN_LEFT )
            self.shape.finish() 
            return

        BASE_LINE = -6

        for ii in range(ep.N_QUESTIONS):

            rr = Rects.grade_entry(ii)
            rr.y0 += BASE_LINE 
            rr.y1 += BASE_LINE 

            nn = grades.question[ii]
            cc = COLOR_CORRECT if nn else COLOR_INCORRECT

            self.shape.insert_textbox( rr, str(nn), color=cc,
                                       fontsize=int( 0.9*rr.height ),
                                       align=fitz.TEXT_ALIGN_CENTER )
    
        tt = grades.total
        final_color = COLOR_CORRECT if tt >= ep.MIN_SCORE else COLOR_INCORRECT

        self.shape.insert_textbox( final_rect, f'{tt:3}',
                                   color    = final_color,
                                   fontsize = final_font,
                                   align    = fitz.TEXT_ALIGN_LEFT )
        self.shape.finish() 

    #--------------------------------------------------------------------------#
    def insert_marks( self, marks, grades, k_lst ):

        if marks.eliminated:
            self.shape.draw_rect( Rects.eliminated() )
            self.shape.finish( width=10, color=COLOR_INCORRECT ) 
            return

        if marks.absent:
            self.shape.draw_rect( Rects.absent() )
            self.shape.finish( width=10, color=COLOR_INCORRECT ) 
            return

        # Draw the correct answer on wrong marks
        for ii in [ ii for ii, nn in enumerate(grades.question) if nn == 0 ]:
            self._draw_key( ii, k_lst[ii] )
        self.shape.finish( width=2, color=(0,0,0), fill=COLOR_KEY, fill_opacity=0.3 ) 

        # Draw correct answers
        for ii in [ ii for ii, nn in enumerate(grades.question) if nn == 1 and k_lst[ii] != -1 ]:
            jj = marks.question[ii][0]
            self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=7, color=COLOR_CORRECT ) 

        # Draw wrong answers
        for ii in [ ii for ii, nn in enumerate(grades.question) if nn == 0 ]:
            for jj in marks.question[ii]:
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=7, color=COLOR_INCORRECT ) 

        # Draw canceled questions
        self._insert_annul( k_lst )

    #--------------------------------------------------------------------------#
    def _draw_annul( self, ii ):

        r1 = Rects.mark_entry( ii, 0 )
        r2 = Rects.mark_entry( ii, 4 )

        p1 = [ r1.x0+5, (r1.y0+r1.y1)/2 ]
        p2 = [ r2.x1-5, (r2.y0+r2.y1)/2 ]

        bb = r1.height/5

        self.shape.draw_squiggle(p1, p2, breadth=bb )

    #--------------------------------------------------------------------------#
    def _insert_annul( self, keys ):
        for ii in [ ii for ii, nn in enumerate(keys) if nn == -1 ]:
            self._draw_annul(ii)
        self.shape.finish( width=5, color=COLOR_ANNUL, closePath=False) 
    
    #--------------------------------------------------------------------------#
    def draw_all_rects(self):
    
        # Masks
        for rr in Rects.masks():
            self.shape.draw_rect( rr )
        self.shape.finish( width=5, color=COLOR_MASK, dashes='[20] 0' ) 

        # Name
        self.shape.draw_rect( Rects.name() )
        self.shape.finish( width=5, color=COLOR_ENTRY ) 
    
        # # Answers box
        # self.shape.draw_rect( Rects.marks_box_left () )
        # self.shape.draw_rect( Rects.marks_box_right() )
        # self.shape.finish( width=5, color=COLOR_MASK ) 
    
        # # Scores box
        # self.shape.draw_rect( Rects.grades_box_left () )
        # self.shape.draw_rect( Rects.grades_box_right() )
        # self.shape.finish( width=5, color=COLOR_MASK ) 
    
        # Score entryes
        for ii in range(ep.N_QUESTIONS):
            self.shape.draw_rect( Rects.grade_entry(ii) )
        self.shape.draw_rect( Rects.full_grade() )
        self.shape.finish( width=5, color=COLOR_SCORE ) 
    
        # Answer entries
        for ii in range(ep.N_QUESTIONS):
            for jj in range(5):
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=5, color=COLOR_ANSWER ) 
    
        # Absent and eliminated
        self.shape.draw_rect( Rects.absent    () )
        self.shape.draw_rect( Rects.eliminated() )
        self.shape.finish( width=5, color=COLOR_ENTRY ) 
    
    #--------------------------------------------------------------------------#
    def _draw_key( self, ii, jj ):

        rr = Rects.mark_entry( ii, jj )
        rr.x0 += 5
        rr.x1 -= 5
        rr.y0 += 5
        rr.y1 -= 5
        self.shape.draw_rect( rr )
    
    #--------------------------------------------------------------------------#
    def draw_answers_key( self, keys ):

        self._insert_annul( keys )
    
        for ii, jj in [ (ii,jj) for ii, jj in enumerate(keys) if jj != -1 ]:
            self._draw_key( ii, jj )
        self.shape.finish( width=2, color=(0,0,0), fill=COLOR_KEY, fill_opacity=0.5 ) 

#------------------------------------------------------------------------------#
