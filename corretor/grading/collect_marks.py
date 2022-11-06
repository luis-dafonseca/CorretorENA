#------------------------------------------------------------------------------#

import numpy as np

import grading.ena_param as ep
from   grading.rects import Rects

_AREA = Rects.mark_entry(0,0).get_area()

#------------------------------------------------------------------------------#
def _is_entry_marked( array, ii, jj ):

    rect = Rects.mark_entry( ii, jj )

    S = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / _AREA

    return S >= 0.5

#------------------------------------------------------------------------------#
def _is_absent( array ):

    rect = Rects.absent()

    S = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rect.get_area()

    return S >= 0.5

#------------------------------------------------------------------------------#
def _is_eliminated( array ):

    rect = Rects.eliminated()

    S = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / rect.get_area()

    return S >= 0.5

#------------------------------------------------------------------------------#
def collect_marks( image ):

    array = image < 220
    marks = []

    for ii in range(ep.N_QUESTIONS):

        M = []

        for jj in range(5):
            if _is_entry_marked( array, ii, jj ):
                M.append(jj)

        marks.append( M )
    
    return marks

#------------------------------------------------------------------------------#
