from geometry import DETAIL, EDGE
from scenes.redraws._w1 import hard_drive

DESCRIPTION = "A small broom sweeps diagonally across the platter window of an external drive."


def draw(s):
    hard_drive(s)
    s.tube([(14, 6, 23), (27, -15, 46)], 2.2, EDGE)
    top = [(11, 2, 23), (19, 7, 23), (10, 24, 18), (-7, 14, 18)]
    toe = [(a, b, c - 3) for a, b, c in top]
    s.face([toe[2], toe[3], top[3], top[2]], EDGE)
    s.face([toe[1], toe[2], top[2], top[1]], EDGE)
    s.face(top, EDGE)
    for t in (.25, .5, .75):
        a = tuple(u + (v - u) * t for u, v in zip(top[0], top[1]))
        b = tuple(u + (v - u) * t for u, v in zip(top[3], top[2]))
        s.line([a, b, (b[0], b[1], b[2] - 3)], DETAIL)
