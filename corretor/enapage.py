#!/usr/bin/python
#------------------------------------------------------------------------------#

import fitz
import cv2
import io
import numpy as np

from rects import Rects

#------------------------------------------------------------------------------#
class ENAPage:

    #--------------------------------------------------------------------------#
    def __init__( self, pdf_doc):

        self.page_rect = Rects.full_page()

        self.page  = pdf_doc.new_page( width=self.page_rect.width, 
                                       height=self.page_rect.height )
        self.shape = self.page.new_shape()

    #--------------------------------------------------------------------------#
    def insert_image( self, img ):

        is_success, buffer = cv2.imencode(".png", img)

        self.page.insert_image( self.page_rect, stream=io.BytesIO(buffer) )

    #--------------------------------------------------------------------------#
    def commit( self ):
        self.shape.commit()

    #--------------------------------------------------------------------------#
    def write_name( self, name ):
    
        R = Rects.name()
        self.shape.draw_rect( R )
        self.shape.finish( color=(1,1,1), fill=(1,1,1) ) 

        self.shape.insert_textbox( R, 
                                   name,
                                   fontsize=int( 0.7*R.height ),
                                   color=(0,0,1),
                                   align=fitz.TEXT_ALIGN_LEFT )
        self.shape.finish( color=(0,0,1) ) 

    #--------------------------------------------------------------------------#
    def write_score( self, score ):
    
        R = Rects.full_score()
        
        C = (0,0,1) if score >= 15 else (1,0,0)

        self.shape.insert_textbox( R, 
                                   str(score), 
                                   fontsize=int( 0.9*R.height ),
                                   color=C,
                                   align=fitz.TEXT_ALIGN_RIGHT )
        self.shape.finish( color=C ) 
    
    #--------------------------------------------------------------------------#
    def draw_rects( self, all_rects=False ):
    
        if all_rects:
    
            # Masks
            for R in Rects.masks():
                self.shape.draw_rect( R )
            self.shape.finish( width=5, color=(1,0,1), dashes="[20] 0" ) 

            # Name
            self.shape.draw_rect( Rects.name() )
            self.shape.finish( width=5, color=(0,0,1) ) 
    
            # Answers box
            self.shape.draw_rect( Rects.answers_box_left () )
            self.shape.draw_rect( Rects.answers_box_right() )
            self.shape.finish( width=5, color=(0,1,0) ) 
    
            # Scores box
            self.shape.draw_rect( Rects.scores_box_left () )
            self.shape.draw_rect( Rects.scores_box_right() )
            self.shape.finish( width=5, color=(0,1,0) ) 
    
            # Score entryes
            for ii in range(30):
                self.shape.draw_rect( Rects.score_entry(ii) )
            self.shape.draw_rect( Rects.full_score() )
            self.shape.finish( width=5, color=(1,0,0) ) 
    
        # Answer and Score entryes
        for ii in range(30):
            for jj in range(5):
                self.shape.draw_rect( Rects.answer_entry( ii, jj ) )
        self.shape.finish( width=5, color=(0,0,1) ) 
    
        # Absent and eliminated
        self.shape.draw_rect( Rects.absent    () )
        self.shape.draw_rect( Rects.eliminated() )
        self.shape.finish( width=5, color=(0,0,1) ) 
    
#------------------------------------------------------------------------------#
