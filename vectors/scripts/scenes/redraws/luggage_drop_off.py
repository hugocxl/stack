from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import luggage

DESCRIPTION = "An upright suitcase rests halfway onto a baggage conveyor with an inward arrow along the belt."


def draw(s):
    for x in (-3, 71):
        s.box(x, 1, -13, 5, 5, 11, 1.2)
        s.box(x, 30, -13, 5, 5, 11, 1.2)
    s.box(-7, -3, -6, 88, 43, 6, 2.5)
    for x in (52, 58, 64, 70, 76):
        s.line([(x, 1, 0), (x, 16, 0)], DETAIL)
        s.line([(x, 32, 0), (x, 36, 0)], DETAIL)
    s.box(-7, -3, -1, 88, 3, 4, 1.1)
    luggage(s)
    arrow(s, [(16, 29, .1), (73, 22, .1)], BOLD, head=11)
    s.box(-7, 37, -1, 88, 3, 3, 1.1, EDGE)
