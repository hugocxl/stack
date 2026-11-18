from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w4 import upright

DESCRIPTION = "A service block branches through a single connector to three matching subordinate blocks."


def draw(s):
    s.line([(-47, 0, 20), (-47, 0, 42), (47, 0, 42), (47, 0, 20)], EDGE)
    s.line([(0, 0, 20), (0, 0, 64)], EDGE)

    for x in (-47, 0, 47):
        upright(s, rounded(x - 15, 0, 30, 21, 2), 0, 9)
        s.line([(x - 8, 0, 10), (x + 8, 0, 10)], DETAIL)

    upright(s, rounded(-25, 64, 50, 26, 3), 0, 13, BOLD)
    for z in (73, 81):
        s.line([(-17, 0, z), (6, 0, z)], DETAIL)
        s.line([(x, 0, k) for x, k in oval(15, z, 1.5, 1.5, count=16)], EDGE)
