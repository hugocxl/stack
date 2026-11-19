from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "A bound lab report shows a specimen vial above paired result and reference columns."


def vial_mark(face, u, v, size, ink=EDGE):
    face.frame(u + size*.23, v + size*.22, size*.54, size*.90, size*.19, ink)
    face.frame(u + size*.17, v, size*.66, size*.22, size*.07, ink)
    face.line([(u + size*.25, v + size*.69), (u + size*.75, v + size*.69)], ink)
    face.line([(u + size*.28, v + size*.49), (u + size*.41, v + size*.49)], DETAIL)


def lab_report(s):
    page = paper(s, 97, pitch=.81, run=.51, angle=-12, depth=8)
    page.slab(rounded(0, 0, 84, 97, 3), 8)
    page.frame(8, 5, 71, 86, 2)
    page.line([(6, 0), (6, 97)], EDGE)
    vial_mark(page, 16, 11, 21, EDGE)
    page.rows(44, 17, (27, 18), step=8, ink=EDGE)
    return page


def draw(s):
    page = lab_report(s)
    page.line([(15, 42), (72, 42)], EDGE)
    page.line([(45, 42), (45, 80)], DETAIL)
    for v in (50, 62, 74):
        page.rows(18, v, (16,), ink=EDGE)
        page.rows(52, v, (14,), ink=DETAIL)
        page.rows(15, v + 6, (57,), ink=DETAIL)
