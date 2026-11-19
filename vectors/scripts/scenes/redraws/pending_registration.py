from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A standing registration form shows three outlined entry fields and a clock badge."


def draw(s):
    s.face([(27, 0, 0), (27, 0, 59), (27, -18, 0)], EDGE)
    s.box(-28, -4, 0, 56, 4, 59, 2)
    s.line([(-19, 0, 48), (0, 0, 48)], EDGE)
    for height in (10, 22, 34):
        bezel(s, -20, 0, height, 40, 7, DETAIL, 1.2)
    badge(s, "clock", 28, 0, 55, 13)
