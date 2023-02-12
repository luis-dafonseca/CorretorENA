#------------------------------------------------------------------------------#

import numpy as np
import grading.rectangles as rects


#------------------------------------------------------------------------------#
class Marks:

    #--------------------------------------------------------------------------#
    def __init__(self):
        self.eliminated = False
        self.absent     = False
        self.question   = []

#--------------------------------------------------------------------------#
def _is_entry_marked( array, ii, jj ):

    rect = rects.MARK[ii][jj]

    aa = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rects.MARK_AREA

    return aa >= 0.5

#--------------------------------------------------------------------------#
def _is_absent( array ):

    rect = rects.ABSENT

    aa = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rects.ABSENT_AREA

    return aa >= 0.5

#--------------------------------------------------------------------------#
def _is_eliminated( array ):

    rect = rects.ELIMINATED

    aa = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rects.ABSENT_AREA

    return aa >= 0.5

#--------------------------------------------------------------------------#
def collect_marks( image ):

    array = image < 220
    marks = Marks()

    if _is_eliminated( array ):
        marks.eliminated = True

    elif _is_absent( array ):
        marks.absent = True

    else:
        for ii in range(rects.N_QUESTIONS):
            M = [ jj for jj in range(5) if _is_entry_marked(array,ii,jj) ]
            marks.question.append( M )

    return marks

#------------------------------------------------------------------------------#
