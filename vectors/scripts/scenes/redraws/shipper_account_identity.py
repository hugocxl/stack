from geometry import DETAIL, EDGE
from scenes.redraws._w1 import carrier_van
from scenes.systems_shapes import bezel

DESCRIPTION = "A clipped carrier ID badge shows a cargo van in its portrait frame."


def draw(s):
    s.box(-26, -6, 0, 52, 6, 64, 3.5)
    bezel(s, -7, 0, 54, 14, 4, EDGE, 2)
    s.tube([(0, -3, 57), (0, -4, 67), (0, -2, 72), (0, 2, 72),
            (0, 3, 66), (0, 1, 57)], 1.5, EDGE)

    bezel(s, -19, 0, 24, 38, 24, DETAIL, 2.3)
    carrier_van(s, -15, 0, 25, 32)
    for z, width in ((15, 28), (8, 20)):
        s.line([(-width / 2, 0, z), (width / 2, 0, z)], DETAIL)
