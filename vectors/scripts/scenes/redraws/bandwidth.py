from geometry import EDGE
from scenes.redraws._w1 import cable_sleeve

DESCRIPTION = "A cutaway network cable exposes four separate channels inside its sleeve."


def draw(s):
    cable_sleeve(s, 0, -31, 10, 24, 21, 3)
    for x, z, spread in ((-10, 32, -6), (-4, 26, -2), (4, 21, 2), (10, 15, 6)):
        s.tube([(x, 10, z), (x, 27, z), (x + spread, 38, z + 1),
                (x + spread, 46, z + 1)], 2.8, EDGE)
