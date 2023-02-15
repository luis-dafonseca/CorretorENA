#------------------------------------------------------------------------------#
'''Test script that reads a model and draw all rectangles on it'''

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import argparse

from grading.ena_form import ENAForm
from grading.pdfs     import InputPDF, OutputPDF

#-----------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('model',  help='PDF file with the answers page model')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    #--------------------------------------------------------------------------#

    model  = InputPDF(args.model)
    output = OutputPDF()

    pixmap = model.get_pixmap(0)

    page = output.new_page()

    form = ENAForm(page)
    form.insert_pixmap(pixmap)
    form.insert_name('RETÂNGULOS', 1)
    form.insert_rects ()
    form.commit()

    output.save(args.output)

    model .close()
    output.close()

#------------------------------------------------------------------------------#
