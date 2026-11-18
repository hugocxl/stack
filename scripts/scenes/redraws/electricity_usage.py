from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import cable_sleeve, meter_register

DESCRIPTION = "A round wall-mounted electricity meter shows a lightning symbol above its analog usage register."


def draw(s):
    s.tube([(0, -8, 0), (0, -8, 23)], 4)
    s.box(-23, -19, 12, 46, 12, 61, 4)
    cable_sleeve(s, 0, -7, 13, 45, 31, 4)
    meter_register(s, y=13)
    glyph(s, "bolt", 0, 13, 57, 9, EDGE)
    s.line([(-11, 13, 30), (11, 13, 30)], DETAIL)
