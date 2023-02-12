#------------------------------------------------------------------------------#
"""
Command line version of the CorretorENA
"""

#------------------------------------------------------------------------------#

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import fitz
import argparse

from grading.grade_exam import grade_exam
from grading.xls_grades import XLSGrades
from tests.cli_progress import CLIProgressBar

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='automatic grading ENA tests')
    parser.add_argument('model',       help='PDF file with answers page model')
    parser.add_argument('keys',        help='TXT file with answers keys')
    parser.add_argument('answers',     help='PDF file with answers')
    parser.add_argument('names',       help='XLS file with names')
    parser.add_argument('cell',        help='Cell address of the fist name')
    parser.add_argument('grades',      help='XLS output file with grades')
    parser.add_argument('annotations', help='PDF output file with annotations')
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    with open(args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    #------------------------------------------------------------------------------#

    model_pdf       = fitz.open(args.model)
    answers_pdf     = fitz.open(args.answers)
    annotations_pdf = fitz.open()

    grades_xls = XLSGrades(args.grades)
    grades_xls.read_names(args.names, args.cell)

    progress_bar = CLIProgressBar()

    grade_exam(
        model_pdf,
        keys,
        answers_pdf,
        annotations_pdf,
        grades_xls,
        progress_bar
    )

    model_pdf.close()
    answers_pdf.close()
    annotations_pdf.save(args.annotations)
    grades_xls.save()

#------------------------------------------------------------------------------#
