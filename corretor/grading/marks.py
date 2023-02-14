#--------------------------------------------------------------------------#
'''Defines the function collect_marks'''

import numpy as np
import grading.rectangles as rects

#--------------------------------------------------------------------------#
def collect_marks(image: np.array) -> tuple[bool, bool, list[list[int]]]:
    '''Collect all marks from image

    Args:
        image (np.array): NumPy array with binary image information

    Return:
        tuple(eliminated, absent, marks)
    '''

    #----------------------------------------------------------------------#
    def is_marked(image: np.array, rect, area: int) -> bool:
        '''Check if given rectangle is marked'''

        MIN_FILL = 0.7

        aa = np.sum(image[rect.y0:rect.y1, rect.x0:rect.x1]) / area

        return aa >= MIN_FILL

    #----------------------------------------------------------------------#
    def is_entry_marked(image: np.array, ii: int, jj: int) -> bool:
        '''Check if option jj of question ii is marked'''

        return is_marked(image, rects.MARK[ii][jj], rects.MARK_AREA)

    #----------------------------------------------------------------------#

    eliminated = is_marked(image, rects.ELIMINATED, rects.ABSENT_AREA)
    absent     = is_marked(image, rects.ABSENT,     rects.ABSENT_AREA)

    marks = []

    if not eliminated and not absent:

        for ii in range(rects.N_QUESTIONS):

            M = [jj for jj in range(5) if is_entry_marked(image, ii, jj)]

            marks.append(M)

    return (eliminated, absent, marks)

#------------------------------------------------------------------------------#
