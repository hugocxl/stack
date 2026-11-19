from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A clock badge overlaps a standing rate meter whose rising bars stop at a bold threshold."


def draw(s):
    s.box(-38, -31, 0, 76, 31, 54, 5)
    bezel(s, -31, 0, 7, 62, 39, EDGE, 2)
    for x, height in ((-23, 8), (-12, 14), (-1, 17), (10, 23), (21, 23)):
        s.line([(x, 0, 13), (x, 0, 13 + height),
                (x + 5, 0, 13 + height), (x + 5, 0, 13)], EDGE)
    s.line([(-25, 0, 13), (27, 0, 13)], DETAIL)
    s.line([(-26, 0, 36), (26, 0, 36)], BOLD)
    badge(s, "clock", 39, -16, 49, 13)
