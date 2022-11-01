#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
import sys
import fitz

sys.path.append('..')

from grading.grade_exam  import grade_exam
from grading.answers_key import AnswersKey
from grading.xls_grades  import XLSGrades

#------------------------------------------------------------------------------#
class CLIProgressBar:

    #--------------------------------------------------------------------------#
    def _print( iteration, 
                total, 
                prefix = '', 
                suffix = '', 
                decimals = 1, 
                length = 100, 
                fill = '█', 
                printEnd = "\r"):
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
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
    
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        
        filledLength = int(length * iteration // total)
        
        bar = fill * filledLength + '-' * (length - filledLength)
        
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        
        # Print New Line on Complete
        if iteration == total: 
            print()

    #--------------------------------------------------------------------------#
    def __init__(self):
        self.total = 0
        self.iter  = 0

    #--------------------------------------------------------------------------#
    def start(self,N):
        self.total = N
        self.iter  = 0
        CLIProgressBar._print( self.iter, self.total, fill='*' )

    #--------------------------------------------------------------------------#
    def step(self):
        self.iter += 1
        CLIProgressBar._print( self.iter, self.total, fill='*' )

#------------------------------------------------------------------------------#

example_dir = "../../docs/example/"

answers_name = example_dir + "exemplo.pdf"
model_name   = example_dir + "modelo.pdf"
input_names  = example_dir + "exemplo.xlsx"
first_name   = 'A2'

name = os.path.basename(answers_name)
name = os.path.splitext(name)[0]

grades_name      = f'{name}-notas.xlsx'
annotations_name = f'{name}-anotacoes.pdf'

#------------------------------------------------------------------------------#

model_pdf       = fitz.open(model_name)
answers_pdf     = fitz.open(answers_name)
annotations_pdf = fitz.open()
grades_xls      = XLSGrades(grades_name)

grades_xls.read_names( input_names, first_name )

#                         1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
answers_key = AnswersKey('D E B B E A A X B D D C D B C C B E E B A A A E E B E B D D')

progress_bar = CLIProgressBar()

grade_exam( model_pdf, answers_key, answers_pdf, annotations_pdf, grades_xls, progress_bar )

model_pdf.close()
answers_pdf.close()
annotations_pdf.save(annotations_name)
grades_xls.save()

#------------------------------------------------------------------------------#
