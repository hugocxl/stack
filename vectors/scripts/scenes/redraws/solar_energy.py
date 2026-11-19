from math import cos, radians, sin

from geometry import EDGE, oval
from scenes.redraws._w1 import screen_point, solar_stand

DESCRIPTION = "A sun with eight rays shines above a tilted photovoltaic panel."


def draw(s):
    solar_stand(s)
    origin = (16, -23, 65)
    s.face([screen_point(*origin, u, v) for u, v in oval(0, 0, 8.5, 8.5, count=36)[:-1]], EDGE)
    for degrees in range(0, 360, 45):
        angle = radians(degrees)
        s.line([screen_point(*origin, r * cos(angle), r * sin(angle)) for r in (12, 16)], EDGE)
