from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import web_globe
from scenes.systems_shapes import bezel

DESCRIPTION = "A browser address bar shows a globe and dot-separated hostname marks beside a check badge."


def draw(s):
    s.box(-45, -13, 0, 90, 13, 24, 5)
    bezel(s, -39, 0, 5, 77, 14, EDGE, 7)
    web_globe(s, -29, 0, 12, 4)
    for x, width in ((-18, 10), (-4, 2), (2, 17), (23, 2), (29, 5)):
        s.line([(x, 0, 12), (x + width, 0, 12)], EDGE)

    badge(s, "check", 43, 0, 22, 12)
