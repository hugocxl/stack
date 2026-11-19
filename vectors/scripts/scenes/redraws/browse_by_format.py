from geometry import EDGE
from scenes.redraws._w4 import nav_thumbnail, nav_window

DESCRIPTION = "A file browser has picture, document, and book tabs above the preview of the selected document."


def draw(s):
    face = nav_window(s, width=107, height=94, angle=-20)
    for u in (9, 69):
        face.frame(u, 51, 29, 21, 2, EDGE)
    face.outline([(8, 10), (99, 10), (99, 48), (66, 48), (66, 73),
                  (41, 73), (41, 48), (8, 48)], EDGE)
    nav_thumbnail(face, 14, 55, 19, 13)
    face.outline([(47, 53), (60, 53), (60, 63), (55, 68), (47, 68)], EDGE)
    face.line([(55, 68), (55, 63), (60, 63)], EDGE)
    face.rows(50, 58, (7,))
    face.outline([(74, 55), (74, 67), (79, 68), (83.5, 66), (88, 68), (93, 67),
                  (93, 55), (88, 56), (83.5, 54), (79, 56)], EDGE)
    face.line([(83.5, 54), (83.5, 66)], EDGE)
    face.rows(17, 38, (42,), ink=EDGE)
    face.rows(17, 30, (67, 58, 65), step=-6)
