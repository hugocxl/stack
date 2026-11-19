from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.systems_shapes import bezel

DESCRIPTION = "A battery pack with two top terminals shows a partially filled charge gauge on its side."


def draw(s):
    s.box(-33, -19, 0, 66, 38, 45, 4)
    s.box(-34, -20, 40, 68, 40, 5, 3)
    for x in (-19, 19):
        s.disk(x, -6, 45, 6.8, 6.8, 7)
        s.ellipse(x, -6, 52, 3.9, 3.9, DETAIL)
    y = 19
    bezel(s, -24, y, 13, 43, 18, EDGE, 2)
    s.line([(19, y, 19), (23, y, 19), (23, y, 25), (19, y, 25)], EDGE)
    for x in (-19, -9, 1):
        bezel(s, x, y, 17, 6, 10, EDGE, .6)
    glyph(s, "bolt", -3, y, 6.5, 4, DETAIL)
