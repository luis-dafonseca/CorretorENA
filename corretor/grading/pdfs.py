#------------------------------------------------------------------------------#
'''Wraps PDF file access'''

import fitz
import grading.rectangles as rects

#------------------------------------------------------------------------------#
class InputPDF:

    def __init__(self, fname: str) -> None:

        self.doc = fitz.open(fname)
        self.page_count = self.doc.page_count

    #--------------------------------------------------------------------------#
    def close(self) -> None:

        self.doc.close()

    #--------------------------------------------------------------------------#
    def get_pixmap(self, ii: int) -> fitz.Pixmap:

        return self.doc[ii].get_pixmap(dpi=rects.DPI, colorspace='GRAY')

#------------------------------------------------------------------------------#
class OutputPDF:

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:

        self.doc = fitz.open()

    #--------------------------------------------------------------------------#
    def save(self, fname: str) -> None:

        self.doc.save(fname)

    #--------------------------------------------------------------------------#
    def close(self) -> None:

        self.doc.close()

    #--------------------------------------------------------------------------#
    def new_page(self) -> fitz.Page:

        return self.doc.new_page(
            width=rects.PAGE.width,
            height=rects.PAGE.height
        )

#------------------------------------------------------------------------------#