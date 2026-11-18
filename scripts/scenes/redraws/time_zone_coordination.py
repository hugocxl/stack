from math import cos, radians, sin

from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A three-dial world clock shows different local hours with the same meeting marker on every dial."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.30, .954), back=(0, -.954, -.30),
                   across=(.94, -.34))
    face.plate(rounded(0, 0, 141, 62, 7), 19)
    for x, hour in ((27, 135), (70, 68), (113, -18)):
        dial = Surface(s, face.point(x, 35, -1.2), rise=face.rise,
                       back=face.back, across=face.across)
        dial.plate(rounded(-16, -15, 32, 30, 15), 2, EDGE)
        dial.stroke([(0, 1), (9 * cos(radians(hour)), 9 * sin(radians(hour)))], BOLD)
        dial.stroke([(0, 1), (10, 4)], BOLD)
        dial.oval(0, 11, 1.8, 1.8, EDGE)
        for u, v in ((-12, 0), (12, 0), (0, -11)):
            dial.oval(u, v, .8, .8)
        face.rules(x - 7, 9, [14])
