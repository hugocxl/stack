from math import cos, radians, sin

from geometry import EDGE
from scenes.redraws._kit import badge, coin

DESCRIPTION = "A freestanding kitchen timer has a marked dial with a check badge at the end of its scale."


def draw(s):
    s.box(8, 1, 0, 44, 22, 8, 3)
    coin(s, 30, 20, 31, 26, depth=14)
    for angle in (9, 42, 75, 108, 141, 174, 207, 240, 273, 306):
        u, v = cos(radians(angle)), sin(radians(angle))
        s.line([(30 + r*u, 20, 31 + r*v) for r in (17, 21)], EDGE)
    s.tube([(27, 21, 22), (33, 21, 41)], 2.6)
    badge(s, "check", 54, 21, 37, 10.5)
