from math import cos, pi, sin

from geometry import EDGE
from scenes.redraws._kit import badge, coin

DESCRIPTION = "A round wall clock with hour marks carries a refresh badge on its right rim."


def draw(s):
    coin(s, 0, 9, 43, 42, depth=9)
    for i in range(4):
        angle = i * pi / 2
        s.line([(r * cos(angle), 9, 43 + r * sin(angle)) for r in (30, 35)], EDGE)
    s.tube([(0, 9, 67), (0, 9, 43), (17, 9, 32)], 1.6, EDGE)
    badge(s, "refresh", 44, 11, 52, 15)
