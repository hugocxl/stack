from geometry import EDGE, oval
from scenes.redraws._kit import coin
from scenes.redraws._w5 import harvest_crate, rect

DESCRIPTION = "A kitchen delivery van has an open sliding cargo door with a produce crate visible inside."


def draw(s):
    for x in (16, 65):
        coin(s, x, 4, 8, 8, 4)
    s.box(0, 2, 9, 54, 28, 32, 2.5)
    s.box(1, 29, 9, 54, 5, 7, 1)
    s.box(0, 29, 15, 7, 5, 27, 1)
    s.box(44, 29, 15, 10, 5, 27, 1)
    s.face([(54, 3, 42), (61, 3, 40), (69, 3, 28), (76, 3, 24),
            (78, 3, 10), (78, 34, 10), (76, 34, 24), (69, 34, 28),
            (61, 34, 40), (54, 34, 42)])
    s.face([(52, 34, 10), (52, 34, 42), (61, 34, 40),
            (69, 34, 28), (76, 34, 24), (78, 34, 10)])
    s.face([(61, 5, 39), (68, 5, 29), (68, 30, 29), (61, 30, 39)])
    s.face([(55, 34, 38), (60, 34, 38), (65, 34, 29), (55, 34, 29)])
    harvest_crate(s, 14, 23, 16, scale=.48)
    s.box(0, 33, 13, 11, 3, 27, 1)
    rect(s, lambda x, z: (x, 36, z), 3, 27, 5, 3, .7)
    s.box(0, 26, 38, 54, 8, 5, 1.2)
    for x in (16, 65):
        coin(s, x, 35, 8, 8.5, 4)
        s.line([(a, 35, b) for a, b in oval(x, 8, 3.7, 3.7)], EDGE)
