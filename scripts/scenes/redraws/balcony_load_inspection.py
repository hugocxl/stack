from geometry import DETAIL, EDGE
from scenes.redraws._w2 import magnifier

DESCRIPTION = "A magnifier frames the triangular support bracket under a projecting railed balcony."


def draw(s):
    s.box(0, 0, 0, 72, 23, 91, 2)
    s.box(22, 23, 49, 24, 1.4, 35, 1)
    s.line([(34, 25, 51), (34, 25, 82)], DETAIL)
    for x in (10, 56):
        s.face([(x, 23, 13), (x, 23, 43), (x, 48, 43), (x, 46, 39),
                (x, 27, 16)], EDGE)
    s.box(3, 23, 43, 65, 31, 6, 1)
    for x in (5, 25, 46, 66):
        s.line([(x, 53, 49), (x, 53, 66)], EDGE)
    for x in (5, 66):
        s.line([(x, 24, 66), (x, 53, 66)], EDGE)
    s.line([(5, 53, 66), (66, 53, 66)], EDGE)

    magnifier(s, 57, 36, 28, 12.5, direction=(.45, -.89))
