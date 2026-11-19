from geometry import EDGE, DETAIL, rounded
from scenes.redraws._w4 import Surface

DESCRIPTION = "A ribboned box cracks open at the front and three rays escape beneath its raised lid."


def draw(s):
    s.box(0, 0, 0, 65, 49, 34, 3)
    s.line([(27, 49, 1), (27, 49, 33)], DETAIL)
    s.line([(39, 49, 1), (39, 49, 33)], DETAIL)
    s.line([(65, 19, 1), (65, 19, 33)], DETAIL)
    s.line([(65, 30, 1), (65, 30, 33)], DETAIL)

    lid = Surface(s, lambda u, v: (u, v * .91, 39 + v * .47))
    lid.slab(rounded(-2, -2, 69, 53, 3), 7)
    for x in (27, 39):
        lid.line([(x, -1), (x, 50)], DETAIL)
        a, b, c = lid.at(x, 51)
        s.line([(a, b, c), (a, b, c - 6.8)], DETAIL)
    lid.line([(-1, 21), (27, 21)], DETAIL)
    lid.line([(39, 21), (66, 21)], DETAIL)

    # The rays clear the open front corner between the rim and the lid.
    s.line([(0, 49, 47), (-16, 49, 44)], EDGE)
    s.line([(0, 49, 43), (-18, 49, 33)], EDGE)
    s.line([(0, 49, 39), (-14, 49, 25)], EDGE)
