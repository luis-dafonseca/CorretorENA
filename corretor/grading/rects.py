#------------------------------------------------------------------------------#
'''Define rectangles pointing to field positions on the ENA form

This module defines the following constants:
    PDI
    PAGE
    REGISTRATION_MASK
    NAME
    NAME_TEXT
    ABSENT
    ELIMINATED
    ABSENT_AREA
    FINAL_GRADE
    MARKS_BOX_LEFT
    MARKS_BOX_RIGHT
    GRADES_BOX_LEFT
    GRADES_BOX_RIGHT
    GRADE
    GRADE_TEXT
    MARK
    MARK_AREA
'''

from fitz import IRect

#------------------------------------------------------------------------------#

PDI  = 300
PAGE = IRect(0, 0, 2481, 3508)

#------------------------------------------------------------------------------#

def _calc_registration_mask() -> IRect:

    x0 =   90
    y0 = 1700
    x1 = x0 + 2305
    y1 = y0 + 1580

    return IRect(x0, y0, x1, y1)

REGISTRATION_MASK = _calc_registration_mask()

#------------------------------------------------------------------------------#

def _calc_name() -> tuple[IRect]:

    x0 =  115
    y0 =  300
    x1 = x0 + 2200
    y1 = y0 +  114

    yt = (y0+y1) // 2

    return (
        IRect(x0, y0, x1, y1),
        IRect(x0, yt, x1, y1)
    )

NAME, NAME_TEXT = _calc_name()

#------------------------------------------------------------------------------#

def _calc_absent_eliminated() -> tuple[IRect]:

    x_absent     =  102
    x_eliminated = 2135
    y = 558
    w = 176
    h = 104

    return (
        IRect(x_absent,     y, x_absent    +w, y+h),
        IRect(x_eliminated, y, x_eliminated+w, y+h)
    )

ABSENT, ELIMINATED = _calc_absent_eliminated()

ABSENT_AREA = ABSENT.get_area()

#------------------------------------------------------------------------------#

def _calc_full_grade() -> IRect:

    x = 1780
    y = 3110
    w =  580
    h =   80

    return IRect(x, y, x+w, y+h)

FINAL_GRADE = _calc_full_grade()

#------------------------------------------------------------------------------#

def _calc_mark_boxes() -> tuple[IRect]:

    x_left  =  300
    x_right = 1483
    y = 1840
    w =  698
    h = 1226

    return (
        IRect(x_left,  y, x_left +w, y+h),
        IRect(x_right, y, x_right+w, y+h)
    )

MARKS_BOX_LEFT, MARKS_BOX_RIGHT = _calc_mark_boxes()

#------------------------------------------------------------------------------#

def _calc_grades_boxes() -> tuple[IRect]:

    x_left  = 1040
    x_right = 2222
    y = 1840
    w =  106
    h = 1226

    return (
        IRect(x_left,  y, x_left +w, y+h),
        IRect(x_right, y, x_right+w, y+h)
    )

GRADES_BOX_LEFT, GRADES_BOX_RIGHT = _calc_grades_boxes()

#------------------------------------------------------------------------------#

def _calc_grades() -> tuple[list[IRect]]:

    grade_box  = []
    grade_text = []
    
    box_height  = 53
    cell_height = 83.6
    cell_base   =  2
    text_base   = -6
    
    for nn in range(30):
    
        if nn < 15:
            rect = GRADES_BOX_LEFT.rect
            ii = nn
        else:
            rect = GRADES_BOX_RIGHT.rect
            ii = nn - 15
    
        rect.y0 += ii * cell_height + cell_base
        rect.y1  = rect.y0 + box_height
    
        grade_box .append(rect.irect)

        rect.y0 += text_base
        rect.y1 += text_base

        grade_text.append(rect.irect)

    return (grade_box, grade_text)


GRADE, GRADE_TEXT = _calc_grades()

#------------------------------------------------------------------------------#

def _calc_marks() -> tuple[list[list[IRect]],int]:

    marks = []

    mark_height =  56
    mark_width  = 106

    cell_height =  83.6
    cell_width  = 148

    for nn in range(30):

        if nn < 15:
            rect = MARKS_BOX_LEFT
            ii = nn
        else:
            rect = MARKS_BOX_RIGHT
            ii = nn - 15

        y0 = rect.y0 + cell_height * ii
        y1 =      y0 + mark_height

        line = []

        xx = rect.x0

        for jj in range(5):

            x0 = xx + cell_width * jj
            x1 = x0 + mark_width

            line.append(IRect(x0,y0,x1,y1))

        marks.append(line.copy())

    return (marks, mark_width*mark_height)

MARK, MARK_AREA = _calc_marks()

#------------------------------------------------------------------------------#