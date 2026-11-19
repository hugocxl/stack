from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import bezier_path, paper

DESCRIPTION = "An environmental certificate carries an embossed leaf seal above two ribbon tails."


def draw(s):
    page = paper(s, 92, pitch=.54, run=.77, angle=4, depth=7)
    page.slab(rounded(0, 0, 92, 92, 3), 7)
    page.frame(6, 6, 80, 80, 1)
    page.rows(15, 22, (62,), ink=EDGE)
    page.rows(15, 32, (53, 26, 27), step=9)
    page.outline([(53, 62), (49, 80), (56, 76), (61, 81), (65, 64)], EDGE)
    page.outline([(66, 62), (68, 80), (73, 76), (80, 80), (74, 62)], EDGE)
    page.slab(rounded(46, 40, 34, 34, 17), 2.7)
    page.oval(63, 57, 13.5, 13.5, EDGE)
    leaf = bezier_path((55, 64), ((54, 56), (57, 48), (72, 48)),
                       ((72, 59), (65, 65), (55, 64)))
    page.line(leaf, BOLD)
    page.line([(53, 67), (63, 57)], EDGE)
