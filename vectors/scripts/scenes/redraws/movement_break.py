from math import cos, radians, sin

from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "An empty office chair stands pushed back on its star base, carrying a clock badge."


def draw(s):
    for a in range(18, 360, 72):
        c, q = cos(radians(a)), sin(radians(a))
        s.tube([(0, 0, 6), (24*c, 24*q, 4)], 2, EDGE)
        s.disk(24*c, 24*q, 0, 3.4, 3.4, 3)
    s.tube([(0, 0, 6), (0, 0, 28)], 2.6, EDGE)
    s.box(-18, -18, 28, 36, 36, 6, 6)
    s.box(-16, -20, 36, 32, 6, 38, 6)
    badge(s, "clock", 24, 6, 64, 12)
