from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import portrait_mark
from scenes.systems_shapes import bezel

DESCRIPTION = "An easel-backed portrait frame carries a plus badge on its bottom corner."


def draw(s):
    s.face([(8, -6, 1), (8, -21, 1), (8, -6, 32)], EDGE)
    s.box(-24, -6, 0, 48, 6, 59, 2)
    bezel(s, -19, 0, 12, 38, 42, DETAIL, 2)
    portrait_mark(s, 0, 0, 33, 14.5, ring=False)
    badge(s, "plus", 24, 1, 10.5, 12)
