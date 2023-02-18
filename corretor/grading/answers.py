#------------------------------------------------------------------------------#
'''Defines the Answers class

This class checks the marks and collect the grades
'''

import numpy as np
import grading.rectangles as rects

MIN_FILL = 0.7

#------------------------------------------------------------------------------#
def keys_str_to_list(keys: list[int] | str) -> list[int]:

    if type(keys) is list:
        return keys

    keys: str       = (''.join(keys.split())).upper()
    keys: list[int] = ['XABCDE'.index(kk)-1 for kk in keys]

    return keys

#------------------------------------------------------------------------------#
class Answers:

    #--------------------------------------------------------------------------#
    def __init__(self, keys: list[int] | str, minimum: int) -> None:
        '''Initialize an Answers object'''

        self.eliminated = False
        self.absent     = False
        self.approved   = False
        self.answers    = [[]]    * rects.N_QUESTIONS
        self.correct    = [False] * rects.N_QUESTIONS
        self.total      = 0
        self.keys       = keys_str_to_list(keys)
        self.min_score  = minimum

    #--------------------------------------------------------------------------#
    def get_score(self) -> int:
        return self.total

    #--------------------------------------------------------------------------#
    def is_eliminated(self) -> bool:
        return self.eliminated

    #--------------------------------------------------------------------------#
    def is_absent(self) -> bool:
        return self.absent

    #--------------------------------------------------------------------------#
    def is_approved(self) -> bool:
        return self.approved

    #--------------------------------------------------------------------------#
    def collect_marks(self, image: np.array) -> None:

        #----------------------------------------------------------------------#
        def is_marked(image: np.array, rect, area: int) -> bool:
            '''Check if given rectangle is marked'''

            aa = np.sum(image[rect.y0:rect.y1, rect.x0:rect.x1]) / area

            return aa >= MIN_FILL

        #----------------------------------------------------------------------#
        def is_entry_marked(image: np.array, ii: int, jj: int) -> bool:
            '''Check if option jj of question ii is marked'''

            return is_marked(image, rects.MARK[ii][jj], rects.MARK_AREA)

        #----------------------------------------------------------------------#

        self.eliminated = is_marked(image, rects.ELIMINATED, rects.ABSENT_AREA)
        self.absent     = is_marked(image, rects.ABSENT,     rects.ABSENT_AREA)

        self.answers = []

        if self.eliminated or self.absent:
            return

        for ii in range(rects.N_QUESTIONS):

            mm = [jj for jj in range(5) if is_entry_marked(image, ii, jj)]

            self.answers.append(mm)

    #--------------------------------------------------------------------------#
    def check_answers(self, image: np.array) -> None:
        '''Check candidate marks and compute its score'''

        self.collect_marks(image)

        if self.eliminated or self.absent:
            return

        for ii, ans in enumerate(self.answers):

            key = self.keys[ii]
            self.correct[ii] = int(key == -1 or (len(ans) == 1 and ans[0] == key))

        self.total    = self.correct.count(True)
        self.approved = self.total >= self.min_score


#------------------------------------------------------------------------------#

