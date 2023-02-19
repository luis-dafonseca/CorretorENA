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

        self.keys       = keys_str_to_list(keys)
        self.min_score  = minimum

        self.reset()

    #--------------------------------------------------------------------------#
    def reset(self) -> None:
        '''Reset candidate marks and scores'''

        self.eliminated = False
        self.absent     = False
        self.approved   = False
        self.answers    = []
        self.correct    = [0] * rects.N_QUESTIONS
        self.total      = 0

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
    def check_answers(self, image: np.array) -> None:
        '''Check candidate marks and compute its score'''

        self.reset()
        self._collect_marks(image)

        if self.eliminated or self.absent:
            return

        for ii, ans in enumerate(self.answers):

            key = self.keys[ii]
            self.correct[ii] = int(key == -1 or (len(ans) == 1 and ans[0] == key))

        self.total    = self.correct.count(True)
        self.approved = self.total >= self.min_score

    #--------------------------------------------------------------------------#
    def _collect_marks(self, image: np.array) -> None:

        #----------------------------------------------------------------------#
        def is_marked(rect) -> bool:
            '''Check if given rectangle is marked'''

            aa = np.mean(image[rect.y0:rect.y1, rect.x0:rect.x1])

            return aa >= MIN_FILL

        #----------------------------------------------------------------------#

        self.eliminated = is_marked(rects.ELIMINATED)
        self.absent     = is_marked(rects.ABSENT    )

        if self.eliminated or self.absent:
            return

        for ii in range(rects.N_QUESTIONS):

            mm = [jj for jj in range(5) if is_marked(rects.MARKS[ii][jj])]

            self.answers.append(mm)


#------------------------------------------------------------------------------#

