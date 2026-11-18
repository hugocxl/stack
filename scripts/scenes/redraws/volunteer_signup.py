from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A clipped volunteer name badge has a plus badge at its corner."


def draw(s):
    s.box(-37, -6, 0, 74, 9, 42, 4)
    bezel(s, -32, 3, 5, 64, 30, DETAIL, 2.5)
    s.box(-10, -4, 36, 20, 9, 14, 2.2)
    s.line([(x, 5, z) for x, z in oval(0, 44, 4.5, 2.1, count=28)], EDGE)
    s.line([(-24, 3, 23), (18, 3, 23)], EDGE)
    s.line([(-17, 3, 14), (11, 3, 14)], DETAIL)
    badge(s, "plus", 35, 1, 34, 11)
