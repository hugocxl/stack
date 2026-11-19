from geometry import EDGE
from scenes.redraws._w4 import attached_panel, file_sheet

DESCRIPTION = "A punched merchandise tag hooks over the upper corner of a document."


def draw(s):
    page = file_sheet(s)
    page.rows(10, 23, (28,), ink=EDGE)
    page.rows(10, 35, (28, 37, 45, 36, 43, 29), step=7)
    tag = attached_panel(page, 3)
    tag.slab([(40, 5), (58, -3), (87, 15), (88, 26), (75, 39), (46, 22)], 4)
    tag.oval(54, 11, 3.5, 3.5, EDGE)
    s.tube([tag.at(54, 11), page.at(49, 3), page.at(45, -4), page.at(41, -2),
            page.at(41, 3)], 1.1)
