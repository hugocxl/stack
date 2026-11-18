from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import portrait_mark
from scenes.systems_shapes import bezel

DESCRIPTION = "A desktop profile nameplate shows a text insertion cursor inside its display-name field."


def draw(s):
    s.face([(34, 0, 0), (34, 0, 34), (34, -21, 0)], EDGE)
    s.face([(-34, 0, 0), (-34, 0, 34), (34, 0, 34), (34, 0, 0)], EDGE)
    portrait_mark(s, -20, 0, 17, 9)
    bezel(s, -7, 0, 10, 34, 14, EDGE, 2)
    s.line([(-2, 0, 17), (11, 0, 17)], DETAIL)
    s.line([(15, 0, 13), (15, 0, 21)], BOLD)
