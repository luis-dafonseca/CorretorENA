#------------------------------------------------------------------------------#

import sys

from pathlib import Path

# Working parameters
#------------------------------------------------------------------------------#

# User home directory

if sys.platform.startswith('win32'):
    HOME = Path.home() / 'Documents'
    if not HOME.is_dir():
        HOME = Path.home()
else:
    HOME = Path.home()

# Resources  parameters
#------------------------------------------------------------------------------#

# Resources path
RESOURCES = Path(__file__).resolve().parent / 'resources'

# Application  parameters
#------------------------------------------------------------------------------#

AUTHOR  = "Luis A. D'Afonseca"
VERSION = '0.0.1 - alpha'
TITLE   = 'Corretor ENA'
MYAPPID = 'Prof_Luis_A_DAfonseca.Corretor_ENA'

ABOUT = f"""{TITLE} é um programa para corrigir as provas do ENA {' '*8}

Desenvolvedor: {AUTHOR}
Versão: {VERSION}
Licença: GNU General Public License - Version 3""" 

# Registration and grading parameters
#------------------------------------------------------------------------------#

DPI        = 300
COLORSPACE = 'GRAY'

N_QUESTIONS = 30
MIN_SCORE   = 15

ENA_KEYS = { 
    '2018': 'CECDXDDABDBCBCAAEACCEAEEEABBDD',
    '2022': 'CEBBEEDEDDBCDBCAEDECAACEBBACAD',
    '2023': 'CBEACBEDCBEEADCCDBADADACDEAEBD' }

#------------------------------------------------------------------------------#
