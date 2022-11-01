#------------------------------------------------------------------------------#

import numpy as np

from grading.rects import Rects

_AREA = Rects.mark_entry(0,0).get_area()

#------------------------------------------------------------------------------#
def _is_entry_marked( array, ii, jj ):

    rect = Rects.mark_entry( ii, jj )

    S = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / _AREA

    return S >= 0.5

#------------------------------------------------------------------------------#
def collect_marks( image ):

    array = image < 220
    marks = []

    for ii in range(30):

        M = []

        for jj in range(5):
            if _is_entry_marked( array, ii, jj ):
                M.append(jj)

        marks.append( M )
    
    return marks

#------------------------------------------------------------------------------#
