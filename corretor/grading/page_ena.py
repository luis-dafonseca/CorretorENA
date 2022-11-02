#!/usr/bin/python
#------------------------------------------------------------------------------#

import fitz
import cv2
import io
import numpy as np

from grading.rects import Rects


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

        is_success, buffer = cv2.imencode( ".png", image )

        self.page.insert_image( self.page_rect, stream=io.BytesIO(buffer) )

    #--------------------------------------------------------------------------#
    def commit( self ):
        self.shape.commit()

    #--------------------------------------------------------------------------#
    def insert_name( self, name ):
    
        R = Rects.name()
        self.shape.draw_rect( R )
        self.shape.finish( color=COLOR_NAME_BG, fill=COLOR_NAME_BG ) 

        self.shape.insert_textbox( R, name, color=COLOR_CORRECT,
                                   fontsize=int( 0.5*R.height ),
                                   align=fitz.TEXT_ALIGN_LEFT )
        self.shape.finish() 

    #--------------------------------------------------------------------------#
    def insert_grades( self, grades ):

        BASE_LINE = -6

        for ii in range(30):

            R = Rects.grade_entry(ii)
            R.y0 += BASE_LINE 
            R.y1 += BASE_LINE 

            N = grades.Q[ii]
            C = COLOR_CORRECT if N else COLOR_INCORRECT

            self.shape.insert_textbox( R, str(N), color=C,
                                       fontsize=int( 0.9*R.height ),
                                       align=fitz.TEXT_ALIGN_CENTER )
    
        R = Rects.full_grade()
        T = grades.T
        C = COLOR_CORRECT if T >= 15 else COLOR_INCORRECT

        self.shape.insert_textbox( R, str(T), color=C,
                                   fontsize=int( 0.9*R.height ),
                                   align=fitz.TEXT_ALIGN_RIGHT )

        self.shape.finish() 

    #--------------------------------------------------------------------------#
    def insert_marks( self, marks, grades, keys ):

        for ii in [ kk for kk, N in enumerate(grades.Q) if N == 0 ]:
            jj = keys[ii]
            if jj == -1:
                seld.draw_annul(ii)
            else:
                self.draw_key( ii, jj )

        for ii in [ kk for kk, N in enumerate(grades.Q) if N == 1 ]:
            for jj in marks[ii]:
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=7, color=COLOR_CORRECT ) 

        for ii in [ kk for kk, N in enumerate(grades.Q) if N == 0 ]:
            for jj in marks[ii]:
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=7, color=COLOR_INCORRECT ) 

    #--------------------------------------------------------------------------#
    def draw_annul( self, ii ):

        R1 = Rects.mark_entry( ii, 0 )
        R2 = Rects.mark_entry( ii, 4 )

        P1 = [ R1.x0+5, (R1.y0+R1.y1)/2 ]
        P2 = [ R2.x1-5, (R2.y0+R2.y1)/2 ]

        B = R1.height/5

        self.shape.draw_squiggle(P1, P2, breadth=B )
        self.shape.finish( width=5, color=COLOR_ANNUL, closePath=False) 

    #--------------------------------------------------------------------------#
    def insert_annul( self, keys ):

        for ii in [ kk for kk, N in enumerate(keys) if N == -1 ]:
            self.draw_annul(ii)
    
    #--------------------------------------------------------------------------#
    def draw_all_rects(self):
    
        # Masks
        for R in Rects.masks():
            self.shape.draw_rect( R )
        self.shape.finish( width=5, color=COLOR_MASK, dashes="[20] 0" ) 

        # Name
        self.shape.draw_rect( Rects.name() )
        self.shape.finish( width=5, color=COLOR_ENTRY ) 
    
        # Answers box
        self.shape.draw_rect( Rects.marks_box_left () )
        self.shape.draw_rect( Rects.marks_box_right() )
        self.shape.finish( width=5, color=COLOR_MASK ) 
    
        # Scores box
        self.shape.draw_rect( Rects.grades_box_left () )
        self.shape.draw_rect( Rects.grades_box_right() )
        self.shape.finish( width=5, color=COLOR_MASK ) 
    
        # Score entryes
        for ii in range(30):
            self.shape.draw_rect( Rects.grade_entry(ii) )
        self.shape.draw_rect( Rects.full_grade() )
        self.shape.finish( width=5, color=COLOR_SCORE ) 
    
        # Answer entries
        for ii in range(30):
            for jj in range(5):
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=5, color=COLOR_ANSWER ) 
    
        # Absent and eliminated
        self.shape.draw_rect( Rects.absent    () )
        self.shape.draw_rect( Rects.eliminated() )
        self.shape.finish( width=5, color=COLOR_ENTRY ) 
    
    #--------------------------------------------------------------------------#
    def draw_key( self, ii, jj ):

        rr = Rects.mark_entry( ii, jj )
        rr.x0 += 5
        rr.x1 -= 5
        rr.y0 += 5
        rr.y1 -= 5
        self.shape.draw_rect( rr )
        self.shape.finish( width=2, color=(0,0,0), fill=COLOR_KEY, fill_opacity=0.5 ) 
    
    #--------------------------------------------------------------------------#
    def draw_answers_key( self, keys ):

        self.insert_annul( keys )
    
        for ii, jj in enumerate(keys):
            if jj == -1:
                self.draw_annul(ii)
            else:
                self.draw_key( ii, jj )

#------------------------------------------------------------------------------#
