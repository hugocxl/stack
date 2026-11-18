from geometry import EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w1 import portrait_mark, smartphone
from scenes.systems_shapes import bezel

DESCRIPTION = "A phone displays a sign-in prompt below an avatar and carries a clock badge."


def draw(s):
    smartphone(s)
    portrait_mark(s, -.8, 4, 25, 6)
    bezel(s, -6, 4, 10, 12, 7, EDGE, 2)
    glyph(s, "arrow", 0, 4, 13.5, 3.4, EDGE)
    badge(s, "clock", 15, 4, 35, 8.5)
