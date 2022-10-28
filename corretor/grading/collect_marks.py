#------------------------------------------------------------------------------#

import numpy as np

from grading.rects import Rects

#------------------------------------------------------------------------------#
def _is_entry_marked( array, ii, jj ):

    rect = Rects.mark_entry( ii, jj )

    S = np.sum( array[ rect.y0:rect.y1, rect.x0:rect.x1 ] ) / 1e6

    return S <= 1

#------------------------------------------------------------------------------#
def collect_marks( image ):

    array = image.astype(np.float32)
    marks = []

    for ii in range(30):

        M = []

        for jj in range(5):
            if _is_entry_marked( array, ii, jj ):
                M.append(jj)

        marks.append( M )
    
    return marks

#------------------------------------------------------------------------------#
