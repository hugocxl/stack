from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, capsule_mark

DESCRIPTION = "An open pocket pill case holds fitted rows of blistered capsules in its lid and base."


def draw(s):
    width = 72
    lid = Surface(s, lambda u, v: (u, -.40*v, 13 + .91*v))
    lid.slab(rounded(0, 0, width, 47, 6), 5)
    lid.frame(6, 5, 60, 36, 5, EDGE)
    for u in (19, 36, 53):
        capsule_mark(lid, u, 23, 8)

    s.box(0, 0, 0, width, 49, 14, 6)
    deck = Surface(s, lambda u, v: (u, v, 14))
    deck.frame(5, 5, 62, 38, 4, EDGE)
    deck.line([(6, 23), (66, 23)], DETAIL)
    for u in (19, 36, 53):
        for v in (14, 33):
            capsule_mark(deck, u, v, 7)
    s.box(30, 47, 5, 12, 4, 7, 1.5)
