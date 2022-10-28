#!/usr/bin/python
#------------------------------------------------------------------------------#

import fitz

#------------------------------------------------------------------------------#
class Rects:

    #--------------------------------------------------------------------------#
    def __init__(self):
        pass

    #--------------------------------------------------------------------------#
    def full_page():
        x =    0
        y =    0
        w = 2481
        h = 3508
        return fitz.IRect( x, y, x+w, y+h )

    #--------------------------------------------------------------------------#
    def masks():

        rects = []

        x =   90
        y = 1700
        w = 2305
        h = 1580
        rects.append( fitz.IRect( x, y, x+w, y+h ) )

        return rects

    #--------------------------------------------------------------------------#
    def marks_box_left():
        x =  300
        y = 1840
        w =  698
        h = 1226
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def marks_box_right():
        x = 1483
        y = 1840
        w =  698
        h = 1226
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def grades_box_left():
        x = 1040
        y = 1840
        w =  106
        h = 1226
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def grades_box_right():
        x = 2222
        y = 1840
        w =  106
        h = 1226
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def grade_entry( N ):

        h = 56
        l = 83.6

        if N <=14:
            box = Rects.grades_box_left()
            ii = N
        else:
            box = Rects.grades_box_right()
            ii = N - 15 

        rect = box

        TEXT_BASE_LINE = 7

        y = rect.y0 + ii * l - TEXT_BASE_LINE

        rect.y0 = int( y )
        rect.y1 = int( y + h )

        return rect
    
    #--------------------------------------------------------------------------#
    def mark_entry( N, jj ):

        he = 56
        hl = 83.6
        we = 106
        wc = 148

        if N <=14:
            box = Rects.marks_box_left()
            ii = N
        else:
            box = Rects.marks_box_right()
            ii = N - 15 

        rect = box

        x = rect.x0 + jj * wc
        y = rect.y0 + ii * hl

        rect.x0 = int( x )
        rect.y0 = int( y )
        rect.x1 = int( x + we )
        rect.y1 = int( y + he )

        return rect
    
    #--------------------------------------------------------------------------#
    def name():
        x =  106
        y =  300
        w = 2200
        h =  114
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def absent():
        x = 102
        y = 558
        w = 176
        h = 104
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def eliminated():
        x = 2135
        y =  558
        w =  176
        h =  104
        return fitz.IRect( x, y, x+w, y+h )
    
    #--------------------------------------------------------------------------#
    def full_grade():
        x = 1780
        y = 3100
        w =  100
        h =   80
        return fitz.IRect( x, y, x+w, y+h )

#------------------------------------------------------------------------------#