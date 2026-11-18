from geometry import DETAIL, EDGE
from scenes.redraws._w2 import outline

DESCRIPTION = "A knobbed calibration weight sits on the raised pan of a digital bench scale."


def draw(s):
    s.box(0, 0, 0, 100, 76, 19, 6)
    outline(s, 18, 76, 4, 43, 11, 2, EDGE)
    s.line([(27, 76, 9), (49, 76, 9)], DETAIL)
    outline(s, 72, 76, 5, 11, 8, 2)
    s.box(9, 7, 19, 82, 60, 5, 5)
    s.disk(50, 35, 24, 22, 22, 6)
    s.disk(50, 35, 30, 18, 18, 22)
    s.disk(50, 35, 52, 5.5, 5.5, 6)
    s.disk(50, 35, 58, 9, 9, 5)
