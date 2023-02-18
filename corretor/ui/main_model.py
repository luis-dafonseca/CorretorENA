#------------------------------------------------------------------------------#
'''Define main interface model'''

import tempfile
from pathlib import Path

from grading.pdfs         import InputPDF, OutputPDF
from grading.spreadsheets import ResultsSheet, read_names_from_spreadsheet
from grading.eval_grades  import eval_grades
from grading.ena_form     import create_fields_page, create_keys_page

from ui.keys_model import KeysModel

#------------------------------------------------------------------------------#
class MainModel:
    '''Main interface model class'''

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:
        '''Initialise main interface model instance'''

        self.has_model   = False
        self.has_exams   = False
        self.has_annot   = False
        self.has_results = False
        self.has_names   = False
        self.done        = False

        self.names: list[str] = []

        self.model: InputPDF | None = None
        self.exams: InputPDF | None = None

        self.fname_annot:   str = ''
        self.fname_results: str = ''

        self.num_exams = 0
        self.num_names = 0

        self.fname_exams = ''

        self.keys_model = KeysModel()

        self.minimum = 15

    #--------------------------------------------------------------------------#
    def __del__(self) -> None:
        '''Delete main interface model instance'''

        if self.has_model: self.model.close()
        if self.has_exams: self.exams.close()

    #--------------------------------------------------------------------------#
    def run(self, progress_bar) -> bool:
        '''Evaluate all exams and save output files'''

        annot   = OutputPDF()
        results = ResultsSheet()

        if self.has_names:
            results.write_names(self.names)

        finished = eval_grades(
            self.model,
            self.keys_model.keys,
            self.minimum,
            self.exams,
            annot,
            results,
            progress_bar
        )

        if finished:
            annot  .save(self.fname_annot)
            results.save(self.fname_results)
            self.done = True

        return finished

    #--------------------------------------------------------------------------#
    def ready_to_run(self) -> bool:
        '''Check if all information needed to evaluation was provided'''

        return (
            self.has_model and
            self.has_exams and
            self.has_annot and
            self.has_results
        )

    #--------------------------------------------------------------------------#
    def set_model(self, fname: str) -> None:
        '''Open PDF model file'''

        new_model = InputPDF(fname)

        nn   = new_model.page_count()
        name = Path(fname).name

        if nn == 0:
            raise ValueError((
                f'O arquivo {name} não é um modelo!\n\n'
                'Ele não contém nenhuma página.\n'
            ))
        elif nn > 1:
            raise ValueError((
                f'O arquivo {name} não é um modelo!\n\n'
                'Ele contém mais do que uma página.\n'
            ))

        if self.has_model:
            self.model.close()

        self.model     = new_model
        self.has_model = True
        self.done      = False

    #--------------------------------------------------------------------------#
    def set_exams(self, fname: str) -> None:
        '''Open PDF with answers of candidates'''

        fpath = Path(fname).resolve()

        new_exams = InputPDF(fpath)

        nn = new_exams.page_count()

        if nn == 0:
            raise ValueError( f'O arquivo {fpath.name} não contém nenhuma página.\n' )

        if self.has_exams:
            self.exams.close()

        self.num_exams   = nn
        self.exams       = new_exams
        self.fname_exams = str(fname)
        self.has_exams   = True
        self.done        = False

        if self.has_names and (self.num_exams != self.num_names):
            raise IndexError((
                f'Cuidado: A quantidade de respostas ({self.num_exams})'
                f'não coincide com a quantidade de nomes ({self.num_names}).\n'
            ))

    #--------------------------------------------------------------------------#
    def set_names(self, fname: str, first_cell: str) -> None:
        '''Load candidates names from spreadsheet'''

        fpath = Path(fname).resolve()

        try:
            self.names = read_names_from_spreadsheet(fpath, first_cell)

        except IOError as er:

            self.names = []

            raise IOError(
                f'Não foi possível ler os nomes do arquivo {fpath.name}!'
                '\n\n{str(er)}'
            )

        self.num_names = len(self.names)
        self.has_names = True
        self.done      = False

        if self.has_exams and (self.num_exams != self.num_names):
            raise IndexError((
                f'Cuidado: A quantidade de respostas ({self.num_exams})'
                f' não coincide com a quantidade de nomes ({self.num_names}).\n'
            ))

    #--------------------------------------------------------------------------#
    def remove_names(self) -> None:
        '''Clear the list of candidates names'''

        self.names     = []
        self.num_names = 0
        self.has_names = False
        self.done      = False

    #--------------------------------------------------------------------------#
    def set_annotations(self, fname: str) -> None:
        '''Define the name of annotations file'''

        self.fname_annot = fname
        self.has_annot   = True
        self.done        = False

    #--------------------------------------------------------------------------#
    def set_results(self, fname: str) -> None:
        '''Define the name of results file'''

        self.fname_results = fname
        self.has_results   = True
        self.done          = False

    #--------------------------------------------------------------------------#
    # def set_keys(self, new_keys: str) -> None:
    #     '''Parse line edit keys string to keys model'''

    #     if self.keys != new_keys:
    #         self.keys = new_keys
    #         self.done = False

    #--------------------------------------------------------------------------#
    def set_minimum(self, value: int) -> None:
        '''Set the minimum number of correct answers to approval'''

        self.minimum = value
        self.done    = False

    #--------------------------------------------------------------------------#
    def get_model_pdf(self) -> str:
        '''Create a PDF with the model page and mark rectangles'''

        self.temp_file = tempfile.NamedTemporaryFile(
            prefix='modelo_',
            suffix='.pdf'
        )

        output = OutputPDF()
        create_fields_page(self.model, output)
        output.save(self.temp_file.name)
        output.close()

        return self.temp_file.name

    #--------------------------------------------------------------------------#
    def get_keys_pdf(self) -> str:
        '''Create a PDF with the model page and answer keys'''

        self.temp_file = tempfile.NamedTemporaryFile(
            prefix='gabarito_',
            suffix='.pdf'
        )

        output = OutputPDF()
        create_keys_page(self.model, output, self.keys_model.keys)
        output.save(self.temp_file.name)
        output.close()

        return self.temp_file.name

    #--------------------------------------------------------------------------#
    def get_exams_pdf(self) -> str:
        '''Return exams PDF file name'''

        return self.fname_exams

    #--------------------------------------------------------------------------#
    def get_annotations_pdf(self) -> str:
        '''Return annotations PDF file name'''

        return self.fname_annot

    #--------------------------------------------------------------------------#
    def get_results_xlsx(self) -> str:
        '''Return results xlsx file name'''

        return self.fname_results

    #--------------------------------------------------------------------------#
    def has_conflict(self) -> bool:
        '''Return if there is conflict between quantity of exams and names'''

        return (
            self.has_exams and
            self.has_names and
            self.num_names != self.num_exams
        )

#------------------------------------------------------------------------------#
