#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QWidget, QMessageBox

import ena_param as ep

#------------------------------------------------------------------------------#
def show_summary(
    parent:   QWidget,
    finished: bool,
    summary:  dict[str, int]
) -> None:
    '''Show correction summary dialog'''

    sep = '\n     '

    if not finished:
        message = f"Correção Cancelada{' '*40}"

    else:
        message = f"Correção Concluída{' '*40}"

        tot = summary['total'     ]
        eli = summary['eliminated']
        abs = summary['absent'    ]
        app = summary['approved'  ]
        rep = summary['reproved'  ]

        if   tot == 1: message += sep +      '1 prova corrigida'
        else:          message += sep + f'{tot} provas corrigidas'

        if   eli == 1: message += sep +      '1 candidato eliminado'
        elif eli >  1: message += sep + f'{eli} candidatos eliminados'

        if   abs == 1: message += sep +      '1 candidato ausente'
        elif abs >  1: message += sep + f'{abs} candidatos ausentes'

        if   app == 1: message += sep +      '1 candidato aprovado'
        elif app >  1: message += sep + f'{app} candidatos aprovados'

        if   rep == 1: message += sep +      '1 candidato reprovado'
        elif rep >  1: message += sep + f'{rep} candidatos reprovados'

    dialog = QMessageBox(parent)
    dialog.setIcon(QMessageBox.Information)
    dialog.setWindowTitle(ep.TITLE)
    dialog.setText(message)
    dialog.show()

#------------------------------------------------------------------------------#
