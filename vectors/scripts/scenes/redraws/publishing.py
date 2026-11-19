from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import face_arrow
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "An outward arrow leaves a folded newspaper with a masthead, a lead photograph, and article columns."


def draw(s):
    page = paper(s, 96, pitch=.55, run=.69, angle=-11, depth=8)
    page.slab(rounded(0, 0, 91, 96, 2), 8)
    page.line([(3, 94), (88, 94)], DETAIL)
    page.rows(9, 13, (58,), ink=EDGE)
    page.line([(9, 22), (82, 22)], DETAIL)
    landscape(page, 9, 30, 39, 33)
    page.rows(55, 33, (26, 20, 26, 22, 18), step=6.5)
    page.rows(9, 71, (73, 62, 48), step=7)

    def point(x, v):
        return page.at(x, 96 - v)

    face_arrow(s, point, [(91, 48), (102, 48), (110, 54), (126, 68)], BOLD, head=10)
