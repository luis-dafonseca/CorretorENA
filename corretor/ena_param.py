#------------------------------------------------------------------------------#

import sys
from pathlib import Path

# Home directory
#------------------------------------------------------------------------------#

HOME = Path.home()

# On windows change home directory to Documents dir
if sys.platform.startswith('win32'):

    new_home= Path.home() / 'Documents'

    if new_home.is_dir():
        HOME = new_home

# Resources
#------------------------------------------------------------------------------#

RESOURCES = Path(__file__).resolve().parent / 'resources'

# Application
#------------------------------------------------------------------------------#

AUTHOR    = "Luis A. D'Afonseca"
VERSION   = '0.0.2 - beta'
TITLE     = 'CorretorENA'
MY_APP_ID = 'Prof_Luis_A_DAfonseca.Corretor_ENA'
APP_URL   = 'https://sites.google.com/view/prof-luis-dafonseca/profmat/Corretor_ENA'
SOURCE    = 'https://github.com/luis-dafonseca/CorretorENA'

ABOUT = f'''
<p>
{TITLE} é um programa para corrigir as provas do ENA <br>
<\p>

<p>
<a href="{APP_URL}">Página do programa</a>    <br>
<a href="{SOURCE}">Código fonte em Python</a> <br>
<\p>

<p>
Desenvolvedor: {AUTHOR} <br>
Versão: {VERSION}       <br>
Licença: GNU General Public License - Version 3
<\p>
'''

# Previous ENA question keys
#------------------------------------------------------------------------------#

ENA_KEYS = {
    '2018': 'CECDXDDABDBCBCAAEACCEAEEEABBDD',
    '2022': 'CEBBEEDEDDBCDBCAEDECAACEBBACAD',
    '2023': 'CBEACBEDCBEEADCCDBADADACDEAEBD'
}

#------------------------------------------------------------------------------#
