#------------------------------------------------------------------------------#

import grading.ena_param as ep

#------------------------------------------------------------------------------#
class Grades:

    #--------------------------------------------------------------------------#
    def __init__(self):
        
        self.question = [0] * ep.N_QUESTIONS
        self.total    = 0

#------------------------------------------------------------------------------#
def keys_str_to_list( k_str ):

    k_str = (''.join(k_str.split())).upper()
    k_lst = [ 'XABCDE'.index(cc)-1 for cc in k_str ]

    return k_lst

#------------------------------------------------------------------------------#
def check_answers( marks, k_lst ):

    grades = Grades()

    if marks.eliminated or marks.absent:
        return grades

    for ii, mm in enumerate( marks.question ):

        kk = k_lst[ii] 
        nn = int( kk == -1 or ( len(mm) == 1 and mm[0] == kk ) )

        grades.question[ii] = nn
        grades.total       += nn

    return grades

#------------------------------------------------------------------------------#

