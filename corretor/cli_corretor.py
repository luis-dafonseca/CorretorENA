#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
import sys
import fitz

from grading.grade_exam  import grade_exam
from grading.answers_key import AnswersKey
from grading.xls_grades  import XLSGrades

#------------------------------------------------------------------------------#
def print_progress_bar( iteration, 
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

#------------------------------------------------------------------------------#
class ProgressBar:

    #--------------------------------------------------------------------------#
    def __init__(self):

        self.total = 0
        self.iter  = 0

    #--------------------------------------------------------------------------#
    def start(self,N):

        self.total = N
        self.iter  = 0

        print_progress_bar( self.iter, self.total, fill='*' )

    #--------------------------------------------------------------------------#
    def step(self):
        
        self.iter += 1

        print_progress_bar( self.iter, self.total, fill='*' )

#------------------------------------------------------------------------------#

pdf_dir = "../../pdf/"

fname = pdf_dir + "small.pdf" if len(sys.argv) < 2 else sys.argv[1]

name = os.path.basename(fname)
name = os.path.splitext(name)[0]

model_name       = pdf_dir + "modelo.pdf"
answers_name     = fname
annotations_name = f'{name}-anotacoes.pdf'
input_names      = pdf_dir + "exemplo.xlsx"
cell_names       = 'A2'
grades_name      = f'{name}-notas.xlsx'

### model_name       = '../../data/2023/modelo.pdf'
### answers_name     = '../../data/2023/respostas-2023.pdf'
### annotations_name = 'ENA_2023.pdf'
### input_names      = '../../data/2023/candidatos.xlsx'
### cell_names       = 'E2'
### grades_name      = 'ENA_2023.xlsx'

#------------------------------------------------------------------------------#

model_pdf       = fitz.open(model_name)
answers_pdf     = fitz.open(answers_name)
annotations_pdf = fitz.open()
grades_xls      = XLSGrades(input_names, cell_names )

#                         1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
answers_key = AnswersKey('d e b b e a a x b d d c d b c c b e e b a a a e e b e b d d') # Teste
answers_key = AnswersKey('C B E A C B E D C B E E A D C C D B A D A D A C D E A E B D') # 2023

progress_bar = ProgressBar()

grade_exam( model_pdf, answers_key, answers_pdf, annotations_pdf, grades_xls, progress_bar )

model_pdf.close()
answers_pdf.close()
annotations_pdf.save(annotations_name)
grades_xls.save(grades_name)

#------------------------------------------------------------------------------#
