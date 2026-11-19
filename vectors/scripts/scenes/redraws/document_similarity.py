from geometry import BOLD, DETAIL
from scenes.redraws._w2 import pack

DESCRIPTION = "Two thick documents expose matching outlined passages in the same position."


def draw(s):
    for x, y, z in ((37, -2, 0), (-8, 12, 12.8)):
        top = pack(s, x, y, z, 55, 73)
        corners = [(x + 9, y + 27), (x + 42, y + 27),
                   (x + 42, y + 44), (x + 9, y + 44)]
        s.line([(u, v, top) for u, v in [*corners, corners[0]]], BOLD)
        for v, length in ((33, 20), (39, 15), (54, 32), (61, 26)):
            s.line([(x + 14, y + v, top), (x + 14 + length, y + v, top)], DETAIL)
