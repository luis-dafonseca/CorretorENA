#------------------------------------------------------------------------------#

# Aplication information
#------------------------------------------------------------------------------#

AUTHOR  = "Luis A. D'Afonseca"
VERSION = '0.0.1 - alpha'
TITLE   = 'Corretor ENA'
MYAPPID = 'Prof_Luis_A_DAfonseca.Corretor_ENA'

ABOUT = f"""{TITLE} é um programa para corrigir as provas do ENA {' '*8}

Desenvolvedor: {AUTHOR}
Versão: {VERSION}
Licença: GNU General Public License - Version 3""" 

# Grading parameters
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
