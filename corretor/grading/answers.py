#------------------------------------------------------------------------------#
'''Defines the Answers class

This class checks the marks and collect the grades
'''

#------------------------------------------------------------------------------#
def keys_str_to_list(keys: list[int] | str) -> list[int]:

    if type(keys) is list:
        return keys

    keys: str       = (''.join(keys.split())).upper()
    keys: list[int] = ['XABCDE'.index(kk)-1 for kk in keys]

    return keys

#------------------------------------------------------------------------------#
class Answers:

    N_QUESTIONS = 30
    MIN_SCORE   = 15

    #--------------------------------------------------------------------------#
    def __init__(self, keys: list[int] | str) -> None:
        '''Initialize an Answers object'''

        self.eliminated = False
        self.absent     = False
        self.approved   = False
        self.answers    = [[]]    * Answers.N_QUESTIONS
        self.correct    = [False] * Answers.N_QUESTIONS
        self.total      = 0
        self.keys       = keys_str_to_list(keys)

    #--------------------------------------------------------------------------#
    def check_answers(
        self,
        eliminated: bool,
        absent: bool,
        marks: list[list[int]]
    ) -> None:
        '''Check candidate marks and compute its score'''

        self.eliminated = eliminated
        self.absent     = absent

        if self.eliminated or self.absent:
            return

        self.answers = marks

        for ii, ans in enumerate(self.answers):

            key = self.keys[ii]
            self.correct[ii] = int(key == -1 or (len(ans) == 1 and ans[0] == key))

        self.total    = self.correct.count(True)
        self.approved = self.total >= Answers.MIN_SCORE

#------------------------------------------------------------------------------#

