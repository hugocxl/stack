from geometry import EDGE, rounded
from scenes.redraws._w4 import magnifier, paper
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A magnifier hovers over a signed medical consent form with a cross in its header."


def draw(s):
    page = paper(s, 98, pitch=.65, run=.68, angle=9, depth=6)
    page.slab(rounded(0, 0, 81, 98, 4), 6)
    medical_cross(page, 19, 18, 9)
    page.rows(36, 15, (34, 24), step=8, ink=EDGE)
    page.rows(12, 39, (56, 44, 49), step=8)
    page.line([(13, 80), (59, 80)], EDGE)
    page.line([(17, 78), (27, 66), (27, 62), (23, 63), (21, 71),
               (24, 75), (33, 70), (34, 74), (42, 69), (45, 73), (55, 69)], EDGE)
    magnifier(page, 71, 40, 18, text=((-3, 20, EDGE), (4, 17, EDGE)))
