from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "Three dice show different outcomes along one curving roll path."


def die(s, x, y, z, pips):
    size = 28
    s.box(x, y, z, size, size, size, 4)
    for u, v in pips:
        s.ellipse(x + 14 + 6*u, y + 14 + 6*v, z + size, 2.3, 2.3, BOLD)
    for dz in (9, 19):
        s.line([(x + 8, y + size, z + dz), (x + 11, y + size, z + dz)], DETAIL)


def draw(s):
    arrow(s, [(8, 48, 1), (44, 56, 1), (76, 49, 1), (89, 31, 1)], EDGE, head=9)
    die(s, 58, -3, 0, ((-1, -1), (0, 0), (1, 1)))
    die(s, 27, 11, 7, ((-1, -1), (-1, 1), (1, -1), (1, 1)))
    die(s, -7, 24, 0, ((0, 0),))
