#------------------------------------------------------------------------------#
'''Define rectangles pointing to field positions on the ENA form

This module defines the following constants:

    DPI
    PAGE
    N_QUESTIONS

    REGISTRATION_MASK

    NAME
    NAME_TEXT

    ABSENT
    ELIMINATED

    MARKS
    MARKS_BOX_LEFT
    MARKS_BOX_RIGHT

    GRADES
    GRADES_TEXT
    GRADES_BOX_LEFT
    GRADES_BOX_RIGHT
    GRADES_FINAL

    BACKGROUND
    BACKGROUND_GRAY

WARNING: Never edit the rectangles from this module!
'''

from fitz import IRect

#------------------------------------------------------------------------------#

DPI  = 300
N_QUESTIONS = 30

PAGE              = IRect( 0,    0, 2481, 3508)
REGISTRATION_MASK = IRect(90, 1700, 2395, 3280)

#------------------------------------------------------------------------------#

NAME      = IRect(115, 320, 2299, 420)
NAME_TEXT = IRect(125, 332, 2299, 393)

ABSENT     = IRect( 102, 558,  278, 662)
ELIMINATED = IRect(2135, 558, 2311, 662)

BACKGROUND      = IRect(1175, 1840, 1315, 3066)
BACKGROUND_GRAY = IRect(1770, 3105, 2365, 3230)

#------------------------------------------------------------------------------#

GRADES_BOX_LEFT  = IRect(1040, 1840, 1146, 3066)
GRADES_BOX_RIGHT = IRect(2222, 1840, 2328, 3066)
GRADES_FINAL     = IRect(1780, 3110, 2360, 3190)

def _calc_grades() -> tuple[list[IRect]]:

    BOX_HEIGHT  = 53
    CELL_HEIGHT = 83.6
    CELL_BASE   =  2
    TEXT_BASE   = -6

    grades_box  = []
    grades_text = []

    rect = GRADES_BOX_LEFT
    base_y0 = rect.y0 + CELL_BASE

    for ii in range(15):

        box_y0  = int(base_y0 + ii * CELL_HEIGHT)
        text_y0 = box_y0 + TEXT_BASE

        grades_box .append(IRect(rect.x0, box_y0,  rect.x1, box_y0 +BOX_HEIGHT))
        grades_text.append(IRect(rect.x0, text_y0, rect.x1, text_y0+BOX_HEIGHT))

    rect = GRADES_BOX_RIGHT

    for ii in range(15):

        box_y0  = int(base_y0 + ii * CELL_HEIGHT)
        text_y0 = box_y0 + TEXT_BASE

        grades_box .append(IRect(rect.x0, box_y0,  rect.x1, box_y0 +BOX_HEIGHT))
        grades_text.append(IRect(rect.x0, text_y0, rect.x1, text_y0+BOX_HEIGHT))

    return (grades_box, grades_text)

GRADES, GRADES_TEXT = _calc_grades()

#------------------------------------------------------------------------------#

MARKS_BOX_LEFT  = IRect( 300, 1840,  998, 3066)
MARKS_BOX_RIGHT = IRect(1483, 1840, 2181, 3066)

def _calc_marks() -> list[list[IRect]]:

    def calc_marks_at_line(xx: int, y0: int) -> list[IRect]:

        MARK_HEIGHT =  56
        MARK_WIDTH  = 106
        CELL_WIDTH  = 148

        line = []

        for jj in range(5):
            x0 = int(xx + CELL_WIDTH * jj)
            line.append(IRect(x0, y0, x0+MARK_WIDTH, y0+MARK_HEIGHT))

        return line

    CELL_HEIGHT = 83.6

    marks = []

    rect = MARKS_BOX_LEFT

    for ii in range(15):
        y0 = int(rect.y0 + CELL_HEIGHT * ii)
        marks.append(calc_marks_at_line(rect.x0, y0))

    rect = MARKS_BOX_RIGHT

    for ii in range(15):
        y0 = int(rect.y0 + CELL_HEIGHT * ii)
        marks.append(calc_marks_at_line(rect.x0, y0))

    return marks

MARKS = _calc_marks()

#------------------------------------------------------------------------------#
