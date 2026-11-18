from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A physical pushpin fastens the end of a toolbar marked with drawing, shape, and selection tools."


def draw(s):
    bar = Surface(s, (0, 0, 0), rise=(-.53, .85), back=(0, -.85, -.53), across=(.96, -.28))
    bar.plate(rounded(0, 0, 108, 32, 5), 8)
    for x in (30, 57, 83):
        bar.stroke([(x, 5), (x, 27)])
    bar.stroke([(8, 9), (10, 16), (21, 24), (25, 20), (15, 11)], EDGE, closed=True)
    bar.rect(36, 8, 15, 16, 2, EDGE)
    bar.stroke([(65, 9), (65, 24), (77, 15), (71, 15), (74, 9), (71, 7), (68, 13)], EDGE, closed=True)
    x, y, z = bar.point(94, 19)
    s.tube([(x, y, z), (x, y, z + 18)], 1.15)
    s.disk(x, y, z + 16, 11, 9, 4)
    s.disk(x, y, z + 20, 5, 4, 10)
    s.disk(x, y, z + 30, 11, 9, 5, BOLD)
