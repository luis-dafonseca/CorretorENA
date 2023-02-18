#------------------------------------------------------------------------------#
'''Wraps PDF file access

Classes:
    InputPDF: Wrap a read only PDF file

        def __init__(self, fname: str) -> None
            Initialise class instance

        def close(self) -> None
            Close PDF file

        def get_pixmap(self, ii: int) -> fitz.Pixmap
            Get page ii as a pixmap object

        def page_count(self) -> int:
            Return the number of pages on PDF

    OutputPDF: Wrap a write only PDF file

        def __init__(self) -> None
            Initialise class instance

        def save(self, fname: str) -> None
            Save PDF file

        def close(self) -> None
            Close PDF file

        def new_page(self) -> fitz.Page
            Create a new page on PDF
'''

import fitz
import grading.rectangles as rects

#------------------------------------------------------------------------------#
class InputPDF:
    '''Wrap a read only PDF file'''

    def __init__(self, fname: str) -> None:
        '''Initialise class instance'''

        self.doc = fitz.open(fname)

    #--------------------------------------------------------------------------#
    def close(self) -> None:
        '''Close PDF file'''

        self.doc.close()

    #--------------------------------------------------------------------------#
    def get_pixmap(self, ii: int) -> fitz.Pixmap:
        '''Get page ii as a pixmap object'''

        return self.doc[ii].get_pixmap(dpi=rects.DPI, colorspace='GRAY')

    #--------------------------------------------------------------------------#
    def page_count(self) -> int:
        '''Return the number of pages on PDF'''

        return self.doc.page_count

#------------------------------------------------------------------------------#
class OutputPDF:
    '''Wrap a write only PDF file'''

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:
        '''Initialise class instance'''

        self.doc = fitz.open()

    #--------------------------------------------------------------------------#
    def save(self, fname: str) -> None:
        '''Save PDF file'''

        self.doc.save(fname)

    #--------------------------------------------------------------------------#
    def close(self) -> None:
        '''Close PDF file'''

        self.doc.close()

    #--------------------------------------------------------------------------#
    def new_page(self) -> fitz.Page:
        '''Create a new page on PDF'''

        return self.doc.new_page(
            width  = rects.PAGE.width,
            height = rects.PAGE.height
        )

#------------------------------------------------------------------------------#