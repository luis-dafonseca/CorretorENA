#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    default: Does nothing
    clean:   Remove temporary files
    help:    Show this message

    draw_keys:    Run test draw_keys.py
    draw_rects:   Run test draw_rects.py
    test_grading: Run test test_grading.py
    cli_corretor: Run test cli_corretor.py
    all:          Run all tests, can take a long time!
"""

#------------------------------------------------------------------------------#

import sys
import os
import argparse
import PyInstaller.__main__ as installer

from pathlib import Path

here = Path(__file__).parent

#------------------------------------------------------------------------------#
def remove_files( path, glob ):
    '''Removes a list of files'''

    for file in Path(path).glob(glob):
        print(f'Removing {file}')
        file.unlink()

#------------------------------------------------------------------------------#
def make_clean():
    '''Remove temporary files'''

    print('Cleaning...')

    remove_files( here, '*.pdf'  )
    remove_files( here, '*.xlsx' )

    remove_files( here / 'data' / 'example', 'exemplo-respostas-anotacoes.pdf' )
    remove_files( here / 'data' / 'example', 'exemplo-respostas-notas.xlsx'    )


    print('Done')

#------------------------------------------------------------------------------#
def run(cmd):
    '''Runs a system command'''

    print(cmd)
    os.system(cmd)

#------------------------------------------------------------------------------#
def run_python(cmd):
    '''Runs python script by system call'''

    run( f'{sys.executable} {cmd}' )

#------------------------------------------------------------------------------#
def make_default():
    '''Build the default target'''
    # print('Making default target...')
    # print('Done')

#------------------------------------------------------------------------------#

model   = here / 'data' / 'example' / 'exemplo-modelo.pdf'
keys    = here / 'data' / 'example' / 'exemplo-gabarito.txt'
answers = here / 'data' / 'example' / 'exemplo-respostas.pdf'
names   = here / 'data' / 'example' / 'exemplo-dados.xlsx'
cell    = 'A2'

#------------------------------------------------------------------------------#
def make_draw_keys():
    '''Run test draw_keys.py'''

    run_python(f'draw_keys.py {model} {keys} draw_keys.pdf')

#------------------------------------------------------------------------------#
def make_draw_rects():
    '''Run test draw_rects.py'''

    run_python(f'draw_rects.py {model} draw_rects.pdf')

#------------------------------------------------------------------------------#
def make_test_grading():
    '''Run test test_grading.py'''

    run_python(f'test_grading.py {model} {keys} {answers} test_grading.pdf --page 2')

#------------------------------------------------------------------------------#
def make_cli_corretor():
    '''Run test cli_corretor.py'''

    grades      = here / 'cli_corretor-grades.xlsx'
    annotations = here / 'cli_corretor-annotations.pdf'

    run_python(f'cli_corretor.py {model} {keys} {answers} {names} {cell} {grades} {annotations}')

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    '''Main function'''

    parser = argparse.ArgumentParser()
    parser.add_argument( 'target', nargs='?', default='default', help='Make target' )
    args = parser.parse_args()

    if args.target == 'default':
        make_default()

    elif args.target == 'clean':
        make_clean()

    elif args.target == 'help':
        print(__doc__)

    elif args.target in [ 'draw_keys', 'draw_keys.py' ]:
        make_draw_keys()

    elif args.target in [ 'draw_rects', 'draw_rects.py' ]:
        make_draw_rects()

    elif args.target in [ 'test_grading', 'test_grading.py' ]:
        make_test_grading()

    elif args.target in [ 'cli_corretor', 'cli_corretor.py' ]:
        make_cli_corretor()

    elif args.target == 'all':
        make_draw_keys()
        make_draw_rects()
        make_test_grading()
        make_cli_corretor()

    else:
        print(f'Error: Unkown target {args.target}!')

#------------------------------------------------------------------------------#
