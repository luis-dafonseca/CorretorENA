#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    help:      Show this message
    clean:     Remove temporary files
    distclean: Remove all files that can be rebuild by make.py
    default:   Build necessary files to execute the program

    dist:      Create distribution package using PyInstaller
"""

#------------------------------------------------------------------------------#

import sys
import os
import argparse
import shutil
import PyInstaller.__main__ as installer

from pathlib import Path

#------------------------------------------------------------------------------#
# Common functions and variables
#------------------------------------------------------------------------------#

here = Path(__file__).parent

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

import tests.make as tests_make

#------------------------------------------------------------------------------#
def make_clean() -> None:
    '''Remove temporary files'''

    print(f'Cleaning {here}...')

    tests_make.make_clean()

    print('Done')

rules['clean'] = make_clean

#------------------------------------------------------------------------------#
def make_distclean() -> None:
    '''Remove all files that can be rebuild by make.py'''

    print(f'Hard cleaning {here}...')

    make_clean()
    tests_make.make_distclean()

    remove_dir( here.parent / 'packaging' )

    print('Done')

rules['distclean'] = make_distclean

#------------------------------------------------------------------------------#
def make_default() -> None:
    '''Build the default target'''

    print('Making default target...')

    for ui_file in (here/'ui').glob('*.ui'):

        py_file = ui_file.with_suffix('.py')

        run( f'pyside6-uic -g python {ui_file} -o {py_file}' )

    print('Done')

rules['default'] = make_default

#------------------------------------------------------------------------------#
def run_pyinstaller(os_name: str, sep: str, one_file: bool = False) -> None:

    path_app       = here          /'corretor.py'
    path_resources = here          /'resources'
    path_icon      = path_resources/'icon.ico'
    path_packaging = here.parent   /'packaging'/os_name

    if one_file:
        path_spec = path_packaging/'onefile'
        name      = 'CorretorENA_Standalone'
    else:
        path_spec = path_packaging/'multifile'
        name      = 'CorretorENA'

    path_work = path_spec/'work'
    path_dist = path_spec/'dist'

    parameters = [str(path_app),
                 f'--name={name}',
                 f'--icon={path_icon}',
                 f'--add-data={path_resources}{sep}resources',
                 f'--specpath={path_spec}',
                 f'--distpath={path_dist}',
                 f'--workpath={path_work}',
                  '--noconfirm',
                  '--windowed' ]

    if one_file:
        parameters.append('--onefile')

    installer.run(parameters)

#------------------------------------------------------------------------------#
def make_dist() -> None:
    '''Execute PyInstaller to build a distribution'''

    if sys.platform.startswith('linux'):
        os_name = 'Linux'
        sep = ':'

    elif sys.platform.startswith('win32'):
        os_name = 'Windows'
        sep = ';'

    else:
        print(f'ERROR: Unknown platform {sys.platform}!')
        return

    print(f'Creating a distribution package for {os_name}...')
    run_pyinstaller(os_name, sep, False)

    print(f'Creating an one file distribution for {os_name}...')
    run_pyinstaller(os_name, sep, True)

    print('Done')

rules['dist'] = make_dist

#------------------------------------------------------------------------------#
# Main function
#------------------------------------------------------------------------------#
def main(target: str) -> None:
    '''Main function'''

    if target in rules:
        rules[target]()
        return

    print(f'Error: Unknown target {target}!')

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    '''Main function'''

    parser = argparse.ArgumentParser()
    parser.add_argument( 'target', nargs='?', default='default', help='Make target' )
    args = parser.parse_args()

    main(args.target)

#------------------------------------------------------------------------------#
