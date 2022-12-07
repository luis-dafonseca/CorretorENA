#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    default: Build py files from resources and ui 
    clean:   Remove temporary files
    help:    Show this message
    dist:    Create ditribution package using PyInstaller
"""

#------------------------------------------------------------------------------#

import sys
import glob
import os
import PyInstaller.__main__ as installer

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
def make_dist():

    if sys.platform.startswith('linux'):
        os_name = 'Linux'
        sep = ':'

    elif sys.platform.startswith('win32'):
        os_name = 'Windows'
        sep = ';'

    else:
        print(f'Unkown platform {sys.platform}!')
        return

    print(f'Creating a distribution package for {os_name}...')

    installer.run([ 'corretor.py',
                    '--name=CorretorENA',
                    '--icon=./resources/icon.ico',
                    '--add-data=resources'+sep+'resources',
                    '--noconfirm',
                    '--windowed' ])

    print('Done')

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    target = 'default' if len(sys.argv) == 1 else sys.argv[1]

    if target == 'default':
        make_default()

    elif target == 'clean':
        make_clean()

    elif target == 'dist':
        make_dist()

    elif target == 'help':
        print(__doc__)

    else:
        print(f'Unkown target {target}!')

#------------------------------------------------------------------------------#
