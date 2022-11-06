#------------------------------------------------------------------------------#

import grading.ena_param as ep

#------------------------------------------------------------------------------#
class Grades:

    #--------------------------------------------------------------------------#
    def __init__(self):
        self.T = 0
        self.Q = [0] * ep.N_QUESTIONS

#------------------------------------------------------------------------------#
class AnswersKey:

    #--------------------------------------------------------------------------#
    def __init__(self, keys):

        if isinstance(keys, str):

            K = (''.join(keys.split())).upper()

            self.keys = []
            for C in K:
                self.keys.append( 'XABCDE'.index(C)-1 )

        else:
            self.keys = keys

    #--------------------------------------------------------------------------#
    def check( self, marks ):

        grades = Grades()
    
        for ii in range(ep.N_QUESTIONS):
    
            M = marks[ii]

            if self.keys[ii] == -1:
                N = 1

            else:
                if len(M) != 1:
                    N = 0
                elif M[0] == self.keys[ii]:
                    N = 1 
                else:
                    N = 0
    
            grades.Q[ii] = N
            grades.T    += N
    
        return grades

#------------------------------------------------------------------------------#

