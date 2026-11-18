from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w1 import open_carton_back, open_carton_front

DESCRIPTION = "A capped glass vial sits in a shaped foam insert inside an open shipping carton."


def draw(s):
    carton = (-34, 34, -26, 26, 31)
    open_carton_back(s, *carton)

    # The foam lifts the vial into view while its circular well holds the base.
    s.box(-31, -23, 1, 62, 46, 27, 4)
    s.face([(x, y, 28) for x, y in rounded(-30, -22, 60, 44, 4)], DETAIL,
           openings=([(x, y, 28) for x, y in oval(0, 0, 13, 13)[:-1]],))

    body = oval(0, 0, 9.5, 9.5)[:-1]
    neck = oval(0, 0, 5.5, 5.5)[:-1]
    s.solid(body, 27, 18, crease=False)
    s.solid(body, 45, 7, top=neck, crease=False)
    s.solid(neck, 52, 4, crease=False)
    s.disk(0, 0, 56, 7, 7, 7)
    s.ellipse(0, 0, 63, 7, 7, EDGE)
    s.ellipse(0, 0, 35, 9.5, 9.5, DETAIL, 0, 180)
    s.line([(7, 6, 36), (7, 6, 43)], DETAIL)
    open_carton_front(s, *carton)
