from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import carrier_van
from scenes.systems_shapes import bezel

DESCRIPTION = "A ring-bound delivery calendar shows a van emblem above a single outlined time slot."


def draw(s):
    s.face([(-30, -5, 58), (30, -5, 58), (30, -30, 0), (-30, -30, 0)], EDGE)
    s.box(-36, -5, 0, 72, 5, 62, 2.5)
    for x in (-22, 22):
        s.tube([(x, -7, 58), (x, -7, 65), (x, -4, 69),
                (x, 1, 67), (x, 2, 60)], 1.45, EDGE)
    s.line([(-30, 0, 37), (30, 0, 37)], EDGE)
    carrier_van(s, -15, 0, 37, 32)

    for z in (7, 17, 27):
        for x in (-29, -9, 11):
            selected = (x, z) == (11, 17)
            bezel(s, x, 0, z, 17, 8, BOLD if selected else DETAIL, .65)
            if selected:
                s.line([(x + 4, 0, z + 4), (x + 13, 0, z + 4)], EDGE)
