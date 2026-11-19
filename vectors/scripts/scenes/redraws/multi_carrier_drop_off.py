from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import carrier_plane, carrier_van
from scenes.systems_shapes import bezel

DESCRIPTION = "A shared parcel drop box has one wide intake slot and a strip of three carrier emblems."


def draw(s):
    s.box(-37, -32, 0, 74, 32, 68, 3.5)
    s.box(-39, -34, 66, 78, 36, 7, 3)
    bezel(s, -29, 0, 40, 58, 17, BOLD, 2)
    s.line([(-25, 0, 51), (25, 0, 51)], EDGE)
    s.line([(-25, 0, 45), (25, 0, 45)], DETAIL)
    bezel(s, -30, 0, 15, 60, 17, EDGE, 1.3)
    for x in (-10, 10):
        s.line([(x, 0, 15), (x, 0, 32)], DETAIL)
    carrier_van(s, -27, 0, 18.5, 15)
    carrier_plane(s, -8, 0, 18, 16)

    s.line([(12, 0, 23), (27, 0, 23), (24, 0, 19),
            (15, 0, 19), (12, 0, 23)], EDGE)
    s.line([(16, 0, 23), (16, 0, 27), (22, 0, 27), (22, 0, 23)], EDGE)
