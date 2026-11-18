from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "An article proof shows a crossed-out sentence with its replacement directly beneath it."


def draw(s):
    page = paper(s, 97, pitch=.61, run=.62, angle=-6, depth=5)
    page.slab(rounded(0, 0, 90, 97, 3), 5)
    page.rows(11, 13, (62,), ink=EDGE)
    page.rows(11, 24, (53, 66), step=7)
    for x, width in ((11, 14), (31, 12), (49, 19)):
        page.frame(x, 46, width, 6, 1.7)
    page.line([(7, 54), (74, 44)], BOLD)
    page.rows(11, 66, (51,), ink=EDGE)
    page.rows(11, 78, (65, 57, 42), step=6)
