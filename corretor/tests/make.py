#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    default: Does nothing
    clean:   Remove temporary files
    help:    Show this message
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
def make_default():
    '''Build the default target'''
    # print('Making default target...')
    # print('Done')

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

    else:
        print(f'Error: Unkown target {args.target}!')

#------------------------------------------------------------------------------#
