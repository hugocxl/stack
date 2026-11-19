from geometry import DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.systems_shapes import bezel

DESCRIPTION = "A fourth server module slides into the open bay of a two-by-two rack."


def draw(s):
    s.box(0, 0, 0, 79, 6, 60, 2)
    s.box(0, 6, 0, 5, 31, 60, 1)
    for z in (0, 28, 56):
        s.box(5, 6, z, 70, 31, 4, 1)
    s.box(37, 6, 4, 5, 31, 52, 1, DETAIL)
    s.box(75, 6, 0, 4, 31, 60, 1)

    for x, y, z in ((7, 11, 6), (43, 11, 6), (7, 11, 34), (43, 29, 34)):
        s.box(x, y, z, 30, 26, 19, 2)
        front = y + 26
        bezel(s, x + 5, front, z + 8, 13, 3, DETAIL, 1.2)
        bezel(s, x + 23, front, z + 7.5, 4, 4, EDGE, 2)
    arrow(s, [(57, 51, 53), (57, 35, 53)], EDGE, head=6)
