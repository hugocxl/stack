from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._sf import ground, plate

DESCRIPTION = "A flat neighborhood map with a street grid carries a standing warning triangle on one block."


def draw(s):
    m = ground(-60, -44, 3)
    plate(s, m, [(0, 0), (120, 0), (120, 88), (0, 88)], 3, (0, 0, -1))
    for u in (40, 80):
        s.line([m(u, 0), m(u, 88)], DETAIL)
    for v in (30, 60):
        s.line([m(0, v), m(120, v)], DETAIL)
    for u, v in ((8, 6), (48, 36), (88, 6), (8, 66), (88, 66)):
        s.line([m(u, v), m(u + 24, v), m(u + 24, v + 18), m(u, v + 18), m(u, v)], DETAIL)
    warning(s, 0, -4, 3, 40)
