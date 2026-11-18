from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import cable_sleeve
from scenes.systems_shapes import bezel

DESCRIPTION = "A round smart electricity meter displays a live load trace beneath a lightning symbol."


def draw(s):
    s.tube([(0, -13, 0), (0, -13, 21)], 3)
    s.box(-25, -20, 10, 50, 12, 52, 3, EDGE)
    cable_sleeve(s, 0, -8, 6, 36, 31, 4)
    bezel(s, -21, 6, 24, 42, 22, EDGE, 2)
    s.line([(-16, 6, 30), (-10, 6, 30), (-6, 6, 35), (0, 6, 32),
            (8, 6, 41), (12, 6, 36), (16, 6, 36)], BOLD)
    glyph(s, "bolt", 0, 6, 55, 6, EDGE)
    for x in (-7, 7):
        s.line([(a, 6, b) for a, b in oval(x, 17, 1.5, 1.5, count=18)], EDGE)
