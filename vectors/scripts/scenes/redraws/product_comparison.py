from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A two-pan balance compares two sizes of the same smartphone."


def draw(s):
    s.disk(0, 0, 0, 17, 13, 5)
    s.solid(rounded(-7, -6, 14, 12, 2), 5, 25, rounded(-3, -4, 6, 8, 2))
    s.tube([(-45, 0, 24), (0, 0, 30), (45, 0, 36)], 2.7)
    for x, z, width, height in ((-45, 24, 23, 41), (45, 36, 28, 50)):
        s.tube([(x, 0, z), (x, 0, z + 6)], 2.4)
        s.disk(x, 0, z + 6, 19, 18, 4)
        bottom = z + 10
        upright(s, rounded(x - width / 2, bottom, width, height, 4), 4, 5)
        face = Surface(s, lambda u, v: (u + x, 4, v + bottom))
        face.frame(3.5 - width / 2, 5, width - 7, height - 13, 2, EDGE)
        face.oval(0, height - 4.5, 1.2, 1.2, DETAIL)
        face.rows(-3.5, 2.7, (7,))
