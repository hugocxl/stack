from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._sf import smooth

DESCRIPTION = "A winding path on the ground runs from an entry ring past a midpoint marker to a check badge."


def draw(s):
    path = smooth([(-44, 28), (-26, 26), (-12, 4), (8, -2), (22, -18), (40, -20)], 10)
    s.line([(x, y, 0) for x, y in path], DETAIL, dashed=True)
    s.ring(-44, 28, 0, 12, 12, 5, 4.5)
    s.disk(8, -2, 0, 7, 7, 4)
    s.disk(40, -20, 0, 9, 9, 3)
    badge(s, "check", 40, -20, 16, 11)
