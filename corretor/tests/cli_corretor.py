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

from tests.cli_progress   import CLIProgressBar
from grading.spreadsheets import ResultsSheet, DataSheet
from grading.grade_exam   import grade_exam

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

    model       = fitz.open(args.model)
    answers     = fitz.open(args.answers)
    annotations = fitz.open()

    sheet = DataSheet()
    names = sheet.read_names(args.names, args.cell)

    results = ResultsSheet()
    results.write_names(names)

    progress_bar = CLIProgressBar()

    grade_exam(
        model,
        keys,
        answers,
        annotations,
        results,
        progress_bar
    )

    model      .close()
    answers    .close()
    annotations.save(args.annotations)
    results    .save(args.grades)

#------------------------------------------------------------------------------#
