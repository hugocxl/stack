from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface

DESCRIPTION = "A divided meal-prep container holds broccoli, grains, and slices of protein in three compartments."


def draw(s):
    s.box(0, 0, 0, 101, 72, 5, 5)
    s.face([(0, 0, 5), (101, 0, 5), (101, 0, 19), (0, 0, 19)])
    s.face([(0, 0, 5), (0, 72, 5), (0, 72, 19), (0, 0, 19)])
    s.box(48, 2, 5, 3, 68, 12, 1)
    s.box(51, 35, 5, 47, 3, 12, 1)

    for x, y in ((16, 18), (30, 32), (19, 52)):
        s.solid(oval(x, y + 3, 3, 3)[:-1], 5, 9, oval(x, y, 4, 4)[:-1])
        crown = [(x + a, y + b) for a, b in
                 ((-9, 0), (-10, -4), (-8, -8), (-4, -9), (-1, -7),
                  (2, -10), (6, -9), (8, -6), (8, -3), (11, -2),
                  (12, 2), (9, 6), (5, 7), (1, 5), (-3, 7),
                  (-7, 6), (-9, 3), (-9, 0))]
        s.face([(a, b, 16) for a, b in crown], EDGE)
        s.line([(x - 3, y - 4, 16), (x - 2, y - 1, 16), (x + 1, y + 1, 16),
                (x + 5, y, 16)], DETAIL)

    s.solid(oval(74, 17, 17, 12)[:-1], 5, 9,
            oval(74, 17, 14, 9)[:-1], EDGE)
    for x, y in ((64, 15), (67, 21), (70, 11), (72, 17), (76, 13),
                 (76, 22), (81, 18), (84, 13)):
        s.ellipse(x, y, 14, 2.3, .95, DETAIL)

    for x, y in ((68, 46), (75, 51), (83, 56)):
        piece = Surface(s, lambda u, v: (x + .79*u - .61*v, y + .61*u + .79*v, 13 - .2*v))
        piece.slab(oval(0, 0, 11, 5.0)[:-1], 4)
        piece.line([(-6, 1), (5, -1)], DETAIL)

    s.face([(101, 0, 5), (101, 72, 5), (101, 72, 19), (101, 0, 19)])
    s.face([(0, 72, 5), (101, 72, 5), (101, 72, 19), (0, 72, 19)])
    s.line([(2, 72, 14), (99, 72, 14)], DETAIL)
