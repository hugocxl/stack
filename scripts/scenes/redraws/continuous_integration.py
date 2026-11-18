from math import cos, pi, sin

from geometry import EDGE
from scenes.redraws._kit import arrow, badge

DESCRIPTION = "A thick figure-eight loop carries a direction arrow and a check badge."


def draw(s):
    def path(t):
        x = 41 * sin(t)
        return x, -x * .35, 27 + .32 * x + 36 * sin(t) * cos(t)

    half = 42
    for start in (pi, 0):
        s.tube([path(start + pi * i / half) for i in range(half + 1)], 4.7, EDGE)
    arrow(s, [path(.72), path(.91), path(1.04)], EDGE, head=4)
    x, y, z = path(4.15)
    badge(s, "check", x - 4, y, z + 8, 12.5)
