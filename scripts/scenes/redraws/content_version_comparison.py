from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A split document spread aligns the same two layouts and outlines the changed line in each version."


def draw(s):
    spread = Surface(s, (0, 0, 0), rise=(-.58, .81), back=(0, -.81, -.58),
                     across=(.99, -.11))
    spread.plate(rounded(0, 0, 114, 74, 5), 8)
    for x in (4, 58):
        page = Surface(s, spread.point(x, 4, -3), rise=spread.rise,
                       back=spread.back, across=spread.across)
        page.plate(rounded(0, 0, 52, 68, 4), 2)
        page.rules(7, 57, [29], ink=EDGE)
        page.rules(7, 47, [37, 29])
        page.rect(5, 22, 41, 12, 1, EDGE)
        page.rules(9, 28, [18 if x == 4 else 33], ink=BOLD)
        page.rules(7, 15, [33, 24])
