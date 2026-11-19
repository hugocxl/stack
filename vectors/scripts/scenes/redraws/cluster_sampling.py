from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "One whole cassette of sample vials is pulled from a three-slot rack and marked with a check."


def cassette(s, x, y, z, ink):
    s.box(x, y, z, 23, 44, 11, 2, ink)
    for offset in (9, 22, 35):
        center = (x + 11.5, y + offset)
        s.disk(*center, z + 11, 4.2, 4.2, 12, EDGE)
        s.disk(*center, z + 21, 4.9, 4.9, 3, EDGE)
        s.ellipse(*center, z + 24, 2.7, 2.7, DETAIL)


def draw(s):
    s.box(0, 0, 0, 91, 54, 9, 3)
    for x in (3, 32, 61):
        s.box(x, 5, 9, 27, 45, 2, 2, DETAIL)
    cassette(s, 5, 5, 11, EDGE)
    cassette(s, 63, 5, 11, EDGE)
    cassette(s, 34, 58, 0, BOLD)
    badge(s, "check", 54, 95, 16, 12)
