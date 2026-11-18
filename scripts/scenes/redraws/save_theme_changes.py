from math import cos, radians, sin

from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A three-leaf theme swatch fan pivots on a rivet and carries a check badge on the front leaf."


def draw(s):
    for angle, depth in ((-30, 10), (0, 6), (30, 2)):
        a = radians(angle)
        face = Surface(s, (0, -depth, 22), rise=(-.25, .97), back=(0, -1, 0), across=(.98, -.18))

        def turn(x, v):
            return (x * cos(a) - v * sin(a), x * sin(a) + v * cos(a))

        face.plate([turn(x, v) for x, v in rounded(-12, -17, 24, 102, 5)], 4)
        for v in (22, 43, 64):
            face.stroke([turn(x, h) for x, h in rounded(-7, v, 14, 14, 2)], EDGE, closed=True)
    face.oval(0, 0, 3, 3, EDGE)
    badge(s, "check", *face.point(*turn(-13, 73), -4), 13)
