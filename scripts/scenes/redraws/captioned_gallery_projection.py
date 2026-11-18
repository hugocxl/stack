from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A pull-down projection screen shows a landscape above a distinct two-line caption band."


def draw(s):
    screen = Surface(s, (0, 0, 0))
    screen.plate(rounded(0, 4, 110, 73, 2), 3)
    s.tube([(-4, -1, 79), (114, -1, 79)], 3.8)
    s.tube([(0, 1, 4), (110, 1, 4)], 1.6)
    s.line([(55, 1, 3), (55, 1, -5)], EDGE)
    screen.oval(55, -7, 2.3, 2.3, EDGE)

    screen.stroke([(12, 40), (40, 65), (62, 46), (81, 57), (98, 41)], DETAIL)
    screen.oval(74, 64, 5, 5, DETAIL)
    screen.rect(21, 12, 68, 22, 2, EDGE)
    for x, v, width in ((30, 26, 22), (56, 26, 24), (36, 19, 13), (53, 19, 21)):
        screen.rules(x, v, [width], ink=BOLD)
