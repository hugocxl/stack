from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge, glyph
from scenes.systems_shapes import bezel

DESCRIPTION = "A loyalty stamp card has four earned stamps in a row leading to a star badge."


def draw(s):
    s.box(-44, -7, 0, 88, 7, 35, 3)
    bezel(s, -38, 0, 7, 76, 21, DETAIL, 2)
    for x in (-29, -13, 3, 19):
        s.line([(a, 0, b) for a, b in oval(x, 17.5, 5.9, 5.9, count=24)], EDGE)
        glyph(s, "check", x, 0, 17.5, 4.1, EDGE)
    badge(s, "star", 39, 2, 18, 11)
