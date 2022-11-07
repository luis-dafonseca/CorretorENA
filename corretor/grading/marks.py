#------------------------------------------------------------------------------#

import numpy as np

import grading.ena_param as ep
from   grading.rects import Rects

_AREA = Rects.mark_entry(0,0).get_area()

#------------------------------------------------------------------------------#
class Marks:

    #--------------------------------------------------------------------------#
    def __init__(self):
        self.eliminated = False
        self.absent     = False
        self.question   = []

#--------------------------------------------------------------------------#
def _is_entry_marked( array, ii, jj ):

    rect = Rects.mark_entry( ii, jj )

    aa = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / _AREA

    return aa >= 0.5

#--------------------------------------------------------------------------#
def _is_absent( array ):

    rect = Rects.absent()

    aa = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rect.get_area()

    return aa >= 0.5

#--------------------------------------------------------------------------#
def _is_eliminated( array ):

    rect = Rects.eliminated()

    aa = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rect.get_area()

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
        for ii in range(ep.N_QUESTIONS):
            M = [ jj for jj in range(5) if _is_entry_marked(array,ii,jj) ]
            marks.question.append( M )
    
    return marks

#------------------------------------------------------------------------------#
