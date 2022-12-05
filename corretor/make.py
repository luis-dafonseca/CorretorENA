#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    default: Build py files from resources and ui 
    clean:   Remove temporary files
    help:    Show this message
"""

#------------------------------------------------------------------------------#

import sys
import glob
import os

#------------------------------------------------------------------------------#
def run(cmd):
    print(cmd)
    os.system(cmd)

#------------------------------------------------------------------------------#
def remove(file):
    print(f'Removing {file}')
    os.remove(file)

#------------------------------------------------------------------------------#
def make_default():
    print('Making default target...')

    for ui_file in glob.glob('./ui/*.ui'):
        py_file = ui_file[:-2] + 'py'
        run(f'pyside6-uic --g python {ui_file} -o {py_file}')
    
    run('pyside6-rcc resources.qrc -o resources_rc.py')
    
    print('Done')

#------------------------------------------------------------------------------#
def make_clean():
    print('Cleaning...')

    clean_files =       glob.glob('./tests/*.pdf' ) 
    clean_files.extend( glob.glob('./tests/*.xlsx') )

    for file in clean_files:
        remove(file)

    print('Done')

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    target = 'default' if len(sys.argv) == 1 else sys.argv[1]

    if target == 'default':
        make_default()

    elif target == 'clean':
        make_clean()

    elif target == 'help':
        print(__doc__)

    else:
        print(f'Unkown target {target}!')

#------------------------------------------------------------------------------#
