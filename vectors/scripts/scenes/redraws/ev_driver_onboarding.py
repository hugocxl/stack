from geometry import EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import car_mark, closed_guide

DESCRIPTION = "A standing driver handbook displays a car and lightning bolt on its cover and carries a plus badge."


def draw(s):
    face = closed_guide(s)
    car_mark(s, face, 28, 28, 1.05)
    glyph(s, "bolt", *face(28, 45), 7, EDGE)
    badge(s, "plus", 49, -14, 61, 12)
