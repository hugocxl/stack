from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import screen_point
from scenes.systems_shapes import bezel

DESCRIPTION = "A curved arrow leads from the old address line to its replacement on an email card."


def draw(s):
    s.box(-34, -7, 0, 68, 7, 50, 2)
    bezel(s, -28, 0, 17, 19, 14, EDGE, 1)
    s.line([(-27, 0, 30), (-18.5, 0, 23), (-10, 0, 30)], EDGE)
    s.line([(-2, 0, 32), (22, 0, 32)], DETAIL)
    s.line([(-2, 0, 17), (22, 0, 17)], EDGE)
    origin = (21, 0, 23)
    offsets = [(0, 9), (5, 7), (8, 3), (8, -2), (6, -5), (1, -7)]
    arrow(s, [screen_point(*origin, u, v) for u, v in offsets], BOLD, head=4.8)
