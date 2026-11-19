from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "An X badge marks the collection door of a parcel pickup locker."


def draw(s):
    s.box(-37, -27, 0, 74, 27, 75, 2.8)
    for x, width in ((-31, 26), (0, 31)):
        for z in (6, 39):
            s.box(x, 0, z, width, 2, 29, 1.2)
            s.line([(x + width - 6, 2, z + 12), (x + width - 6, 2, z + 19)], EDGE)
    bezel(s, -25, 2, 47, 14, 11, DETAIL, 1)
    s.line([(-21, 2, 58), (-21, 2, 53), (-15, 2, 53), (-15, 2, 58)], DETAIL)
    badge(s, "x", 41, 4, 68, 11)
