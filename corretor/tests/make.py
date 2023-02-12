#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    help:      Show this message
    clean:     Remove temporary files
    distclean: Remove all files that can be rebuild by make.py
    default:   Build necessary files to execute the program

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
import shutil

from pathlib import Path

#------------------------------------------------------------------------------#
# Common functions and variables
#------------------------------------------------------------------------------#

here   = Path(__file__).parent

output = here / 'output'
output.mkdir(parents=True, exist_ok=True)

#------------------------------------------------------------------------------#
def remove_dir(path: Path) -> None:
    '''Recursively removes a directory'''

    if path.is_dir():
        print(f'Removing directory {path}')
        shutil.rmtree(path)
    else:
        print(f"{path} don't exists")

#------------------------------------------------------------------------------#
def remove_files(path: Path, glob: str) -> None:
    '''Removes a list of files'''

    for file in Path(path).glob(glob):
        print(f'Removing {file}')
        file.unlink()

#------------------------------------------------------------------------------#
def run(cmd: str) -> None:
    '''Runs a system command'''

    print(cmd)
    os.system(cmd)

#------------------------------------------------------------------------------#
def run_python(cmd: str) -> None:
    '''Runs python script by system call'''

    run( f'{sys.executable} {cmd}' )

#------------------------------------------------------------------------------#
# Targets
#------------------------------------------------------------------------------#

rules = {}
rules['help'] = lambda: print(__doc__)

#------------------------------------------------------------------------------#
def make_clean() -> None:
    '''Remove temporary files'''

    print(f'Cleaning {here}...')

    remove_files( output, '*.pdf'  )
    remove_files( output, '*.xlsx' )
    remove_files( here / 'data' / 'example', 'exemplo-respostas-anotacoes.pdf' )
    remove_files( here / 'data' / 'example', 'exemplo-respostas-notas.xlsx'    )

    print('Done')

rules['clean'] = make_clean

#------------------------------------------------------------------------------#
def make_distclean() -> None:
    '''Remove all files that can be rebuild by make.py'''

    print(f'Hard cleaning {here}...')
    make_clean()
    print('Done')

rules['distclean'] = make_distclean

#------------------------------------------------------------------------------#
def make_default() -> None:
    '''Build the default target'''

    print('Nothing to be done')

rules['default'] = make_default

#------------------------------------------------------------------------------#
# Tests
#------------------------------------------------------------------------------#

tests = {}

example = here / 'data' / 'example'

model   = example / 'exemplo-modelo.pdf'
keys    = example / 'exemplo-gabarito.txt'
answers = example / 'exemplo-respostas.pdf'
names   = example / 'exemplo-dados.xlsx'
cell    = 'A2'

#------------------------------------------------------------------------------#
def make_draw_keys() -> None:
    '''Run test draw_keys.py'''

    run_python(f'draw_keys.py {model} {keys} draw_keys.pdf')

tests['draw_keys'] = make_draw_keys

#------------------------------------------------------------------------------#
def make_draw_rects() -> None:
    '''Run test draw_rects.py'''

    run_python(f'draw_rects.py {model} draw_rects.pdf')

tests['draw_rects'] = make_draw_rects

#------------------------------------------------------------------------------#
def make_test_grading() -> None:
    '''Run test test_grading.py'''

    run_python(f'test_grading.py {model} {keys} {answers} test_grading.pdf --page 2')

tests['test_grading'] = make_test_grading

#------------------------------------------------------------------------------#
def make_cli_corretor() -> None:
    '''Run test cli_corretor.py'''

    grades      = output / 'cli_corretor-notas.xlsx'
    annotations = output / 'cli_corretor-anotacoes.pdf'

    run_python(f'cli_corretor.py {model} {keys} {answers} {names} {cell} {grades} {annotations}')

tests['cli_corretor'] = make_cli_corretor

#------------------------------------------------------------------------------#
# Main function
#------------------------------------------------------------------------------#
def main(target: str) -> None:
    '''Main function'''

    if target in rules:
        rules[target]()
        return

    target = target.replace('.py','')

    if target in tests:
        tests[target]()
        return

    if target == 'all':
        for test in tests.values():
            test()
        return

    print(f'Error: Unknown target {target}!')

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( 'target', nargs='?', default='default', help='Make target' )
    args = parser.parse_args()

    main(args.target)

#------------------------------------------------------------------------------#
