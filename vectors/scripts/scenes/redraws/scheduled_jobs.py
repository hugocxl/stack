from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import prompt
from scenes.systems_shapes import bezel

DESCRIPTION = "A standing desk calendar shows a command prompt inside one scheduled time block."


def draw(s):
    s.face([(-31, -21, 0), (31, -21, 0), (31, -6, 54), (-31, -6, 54)], EDGE)
    s.box(-32, -8, 0, 64, 8, 55, 2)
    for x in (-19, 19):
        s.tube([(x, -6, 51), (x, -6, 60), (x, 2, 60), (x, 3, 55),
                (x, 3, 49)], 1.5, EDGE)
    s.line([(-26, 0, 44), (26, 0, 44)], EDGE)
    bezel(s, -25, 0, 7, 50, 32, EDGE, 1)
    s.line([(0, 0, 7), (0, 0, 39)], DETAIL)
    s.line([(-25, 0, 23), (25, 0, 23)], DETAIL)
    prompt(s, 5, 0, 31, 5, BOLD)
