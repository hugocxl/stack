from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A graduated specimen vial with a conical bottom and ribbed screw cap carries a check badge."


def draw(s):
    s.disk(0, 0, 0, 5, 5, 3, DETAIL)
    s.solid(oval(0, 0, 5, 5)[:-1], 3, 19, oval(0, 0, 17, 17)[:-1], crease=False)
    s.disk(0, 0, 22, 17, 17, 48)
    s.ellipse(0, 0, 22, 17, 17, DETAIL, -45, 135)
    s.ellipse(0, 0, 34, 17, 17, EDGE, -45, 135)
    for z in (41, 48, 55, 62):
        s.ellipse(0, 0, z, 17, 17, DETAIL, 5, 40 if z % 2 else 54)
    s.disk(0, 0, 69, 20, 20, 11)
    for a in (0, 20, 40, 60, 80, 100, 120):
        x, y = 20*cos(radians(a)), 20*sin(radians(a))
        s.line([(x, y, 71), (x, y, 76)], DETAIL)
    badge(s, "check", 22, 2, 60, 13)
