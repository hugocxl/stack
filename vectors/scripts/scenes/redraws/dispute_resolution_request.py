from geometry import EDGE
from scenes.redraws._w3 import clipboard

DESCRIPTION = "A standing clipboard holds a dispute form with two facing speech bubbles and a signature line."


def draw(s):
    page = clipboard(s)
    for x, direction, v in ((14, 1, 51), (75, -1, 47)):
        bubble = [(0, 3), (3, 0), (12, 0), (21, -6), (21, 0), (25, 0),
                  (28, 3), (28, 15), (25, 18), (3, 18), (0, 15)]
        page.stroke([(x + direction * u, v + dv) for u, dv in bubble], EDGE, closed=True)
        for offset, length in ((11, 20), (6, 13)):
            page.stroke([(x + direction * 4, v + offset),
                         (x + direction * length, v + offset)])

    page.rules(14, 35, [60, 49])
    page.stroke([(17, 14), (22, 16), (25, 21), (22, 22), (19, 18), (19, 14),
                 (24, 14), (29, 17), (32, 14), (38, 15), (42, 17)], EDGE)
    page.rules(14, 10, [55], ink=EDGE)
