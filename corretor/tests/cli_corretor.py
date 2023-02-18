#------------------------------------------------------------------------------#
'''Command line version of the CorretorENA'''

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import argparse

from grading.spreadsheets import ResultsSheet, read_names_from_spreadsheet
from grading.pdfs         import InputPDF, OutputPDF
from grading.eval_grades  import eval_grades

from tests.cli_progress import CLIProgressBar

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='automatic grading ENA tests')
    parser.add_argument('model',   help='PDF file with answers page model')
    parser.add_argument('keys',    help='TXT file with answers keys')
    parser.add_argument('exam',    help='PDF file with answers')
    parser.add_argument('names',   help='XLS file with names')
    parser.add_argument('cell',    help='Cell address of the fist name')
    parser.add_argument('results', help='XLS output file with results')
    parser.add_argument('annot',   help='PDF output file with annotations')
    parser.add_argument('--min',   help='Minimum number of correct answers', type=int, default=15)
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    with open(args.keys, 'r') as file:
        keys = file.read().replace('\n', '')

    #------------------------------------------------------------------------------#

    model = InputPDF(args.model)
    exam  = InputPDF(args.exam)
    annot = OutputPDF()

    names = read_names_from_spreadsheet(args.names, args.cell)

    results = ResultsSheet()
    results.write_names(names)

    progress_bar = CLIProgressBar()

    _ = eval_grades(
        model,
        keys,
        args.min,
        exam,
        annot,
        results,
        progress_bar
    )

    results.save(args.results)
    annot  .save(args.annot)

    model.close()
    exam .close()
    annot.close()

#------------------------------------------------------------------------------#
