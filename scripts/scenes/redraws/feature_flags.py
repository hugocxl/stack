from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import coin
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A feature control shows a raised flag emblem next to a single on-off switch."


def draw(s):
    point = lambda x, z: (x, 0, z)
    panel(s, rounded(0, 0, 88, 39, 5), point, 12)
    s.line([point(16, 8), point(16, 32)], EDGE)
    s.face([point(16, 31), point(34, 31), point(30, 25),
            point(34, 19), point(16, 19)], EDGE)
    rect(s, point, 43, 10, 35, 19, 9.5)
    s.line([point(51, 19.5), point(58, 19.5)], DETAIL)
    coin(s, 68.5, 2.4, 19.5, 7.3, depth=2.3)
