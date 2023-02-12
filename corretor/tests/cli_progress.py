#------------------------------------------------------------------------------#
"""
Define a progress bar class for the command line version of the CorretorENA
"""

#------------------------------------------------------------------------------#
class CLIProgressBar:
    '''Class to produce a text progress bar on terminal'''

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:
        '''Initialize the Progress Bar'''

        self.total = 0
        self.iter  = 0

    #--------------------------------------------------------------------------#
    def start(self, N: int) -> None:
        '''Start the Progess Bar providing the number of steps'''

        self.total = N
        self.iter  = 0
        self.show( self.iter, self.total )

    #--------------------------------------------------------------------------#
    def step(self) -> None:
        '''Add one step to Progress Bar'''

        self.iter += 1
        self.show( self.iter, self.total )

        return True

    #--------------------------------------------------------------------------#
    def show(self,
             iteration: int,
             total: int,
             prefix: str   = '',
             suffix: str   = '',
             decimals: int = 1,
             length: int   = 100,
             fill: str     = '*',
             printEnd: str = '\r') -> None:
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. '\r', '\r\n') (Str)
        """

        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))

        filledLength = int(length * iteration // total)

        bar = fill * filledLength + '-' * (length - filledLength)

        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

        # Print New Line on Complete
        if iteration == total:
            print()

#------------------------------------------------------------------------------#