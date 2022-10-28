#!/usr/bin/python
#------------------------------------------------------------------------------#

import fitz
import cv2
import io
import numpy as np

from grading.rects import Rects

BLACK   = (0,0,0)
WHITE   = (1,1,1)
RED     = (1,0,0)
GREEN   = (0,1,0)
BLUE    = (0,0,1)
MAGENTA = (1,0,1)

#------------------------------------------------------------------------------#
class PageENA:

    #--------------------------------------------------------------------------#
    def __init__( self, pdf_doc):

        self.page_rect = Rects.full_page()

        self.page  = pdf_doc.new_page( width=self.page_rect.width, 
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
        self.shape.finish( color=WHITE, fill=WHITE ) 

        self.shape.insert_textbox( R, name, color=BLUE,
                                   fontsize=int( 0.7*R.height ),
                                   align=fitz.TEXT_ALIGN_LEFT )
        self.shape.finish() 

    #--------------------------------------------------------------------------#
    def insert_grades( self, grades ):

        for ii in range(30):

            R = Rects.grade_entry(ii)
            N = grades.Q[ii]
            C = BLUE if N else RED

            self.shape.insert_textbox( R, str(N), color=C,
                                       fontsize=int( 0.9*R.height ),
                                       align=fitz.TEXT_ALIGN_CENTER )
    
        R = Rects.full_grade()
        T = grades.T
        C = BLUE if T >= 15 else RED

        self.shape.insert_textbox( R, str(T), color=C,
                                   fontsize=int( 0.9*R.height ),
                                   align=fitz.TEXT_ALIGN_RIGHT )

        self.shape.finish() 

    #--------------------------------------------------------------------------#
    def insert_marks( self, marks, grades ):

        for ii in [ kk for kk, N in enumerate(grades.Q) if N == 1 ]:
            for jj in marks[ii]:
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )

        self.shape.finish( width=5, color=BLUE ) 

        for ii in [ kk for kk, N in enumerate(grades.Q) if N == 0 ]:
             for jj in marks[ii]:
                     self.shape.draw_rect( Rects.mark_entry( ii, jj ) )

        self.shape.finish( width=5, color=RED ) 

    #--------------------------------------------------------------------------#
    def insert_annul( self, keys ):

        for ii in [ kk for kk, N in enumerate(keys) if N == -1 ]:
                
            R1 = Rects.mark_entry( ii, 0 )
            R2 = Rects.mark_entry( ii, 4 )

            P1 = [ R1.x0, (R1.y0+R1.y1)/2 ]
            P2 = [ R2.x1, (R2.y0+R2.y1)/2 ]

            B = R1.height/5

            self.shape.draw_squiggle(P1, P2, breadth=B )

        self.shape.finish( width=5, color=MAGENTA, closePath=False) 
    
    #--------------------------------------------------------------------------#
    def insert_rects( self, all_rects=False ):
    
        if all_rects:
    
            # Masks
            for R in Rects.masks():
                self.shape.draw_rect( R )
            self.shape.finish( width=5, color=(1,0,1), dashes="[20] 0" ) 

            # Name
            self.shape.draw_rect( Rects.name() )
            self.shape.finish( width=5, color=(0,0,1) ) 
    
            # Answers box
            self.shape.draw_rect( Rects.marks_box_left () )
            self.shape.draw_rect( Rects.marks_box_right() )
            self.shape.finish( width=5, color=(0,1,0) ) 
    
            # Scores box
            self.shape.draw_rect( Rects.grades_box_left () )
            self.shape.draw_rect( Rects.grades_box_right() )
            self.shape.finish( width=5, color=(0,1,0) ) 
    
            # Score entryes
            for ii in range(30):
                self.shape.draw_rect( Rects.grade_entry(ii) )
            self.shape.draw_rect( Rects.full_grade() )
            self.shape.finish( width=5, color=(1,0,0) ) 
    
        # Answer and Score entryes
        for ii in range(30):
            for jj in range(5):
                self.shape.draw_rect( Rects.mark_entry( ii, jj ) )
        self.shape.finish( width=5, color=(0,0,1) ) 
    
        # Absent and eliminated
        self.shape.draw_rect( Rects.absent    () )
        self.shape.draw_rect( Rects.eliminated() )
        self.shape.finish( width=5, color=(0,0,1) ) 
    
#------------------------------------------------------------------------------#
