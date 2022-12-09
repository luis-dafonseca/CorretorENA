#------------------------------------------------------------------------------#

"""
Command line version of the Corretor ENA
"""

#------------------------------------------------------------------------------#

import sys
import fitz
import argparse

sys.path.append('..')

from grading.grade_exam import grade_exam
from grading.xls_grades import XLSGrades

#------------------------------------------------------------------------------#
class CLIProgressBar:
    '''
    Class to produce a text progress bar on terminal
    '''

    #--------------------------------------------------------------------------#
    def __init__(self):

        self.total = 0
        self.iter  = 0

    #--------------------------------------------------------------------------#
    def start(self,N):

        self.total = N
        self.iter  = 0
        self.show( self.iter, self.total )

    #--------------------------------------------------------------------------#
    def step(self):

        self.iter += 1
        self.show( self.iter, self.total )

        return True

    #--------------------------------------------------------------------------#
    def show( self,
              iteration, 
              total, 
              prefix   = '', 
              suffix   = '', 
              decimals = 1, 
              length   = 100, 
              fill     = '*', 
              printEnd = '\r'):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. '\r', '\r\n') (Str)
        """
    
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        
        filledLength = int(length * iteration // total)
        
        bar = fill * filledLength + '-' * (length - filledLength)
        
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        
        # Print New Line on Complete
        if iteration == total: 
            print()

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='automatic grading ENA tests')
    parser.add_argument( 'model',       help='PDF file with answers page model' )
    parser.add_argument( 'keys',        help='TXT file with answers keys' )
    parser.add_argument( 'answers',     help='PDF file with answers' )
    parser.add_argument( 'names',       help='XLS file with names' )
    parser.add_argument( 'cell',        help='Cell address of the fist name' )
    parser.add_argument( 'grades',      help='XLS output file with grades' )
    parser.add_argument( 'annotations', help='PDF output file with annotations' )
    args = parser.parse_args()
    
    #--------------------------------------------------------------------------#

    with open( args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    #------------------------------------------------------------------------------#
    
    model_pdf       = fitz.open(args.model)
    answers_pdf     = fitz.open(args.answers)
    annotations_pdf = fitz.open()
    grades_xls      = XLSGrades(args.grades)
    
    grades_xls.read_names( args.names, args.cell )
    
    progress_bar = CLIProgressBar()
    
    grade_exam( model_pdf, keys, answers_pdf, annotations_pdf, grades_xls, progress_bar )
    
    model_pdf.close()
    answers_pdf.close()
    annotations_pdf.save(args.annotations)
    grades_xls.save()

#------------------------------------------------------------------------------#
