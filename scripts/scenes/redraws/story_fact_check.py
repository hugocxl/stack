from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import magnifier, paper

DESCRIPTION = "A magnifier enlarges a single sentence on a typeset article."


def draw(s):
    page = paper(s, 105, pitch=.79, run=.49, angle=3, depth=6)
    page.slab(rounded(0, 0, 78, 105, 3), 6)
    page.rows(10, 16, (49,), ink=BOLD)
    page.rows(10, 25, (33,), ink=EDGE)
    page.rows(10, 40, (49, 52, 55, 45, 51, 49, 31), step=8)
    magnifier(page, 61, 54, 23,
              text=((-10, 19, DETAIL), (0, 29, BOLD), (10, 23, DETAIL)))
