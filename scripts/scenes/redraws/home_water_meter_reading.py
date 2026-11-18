from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import droplet

DESCRIPTION = "A domestic water meter joins two pipes and displays consumption on an angled analog register."


def draw(s):
    s.tube([(-44, 0, 10), (44, 0, 10)], 4.3)
    for x in (-30, 22):
        s.box(x, -7, 3, 8, 14, 14, 2)
    s.disk(0, 0, 0, 24, 19, 18)

    def dial(x, y):
        return (x, y, 25 - .34 * y)

    s.face([dial(x, y) for x, y in oval(0, 0, 24, 19, count=64)[:-1]], EDGE)
    s.line([dial(x, y) for x, y in oval(0, 0, 20.5, 15.5, count=60)], DETAIL)
    s.line([dial(x, y) for x, y in oval(0, 0, 16, 11.5, 183, 340, 32)], EDGE)
    for angle in (189, 222, 255, 288, 321):
        c, n = cos(radians(angle)), sin(radians(angle))
        s.line([dial(16 * c, 11.5 * n), dial(12 * c, 8.5 * n)], EDGE)
    s.line([dial(0, 0), dial(5, -8.2)], BOLD)
    droplet(s, lambda u, v: dial(-2 + 10*u, 7 - 7*v), EDGE)
