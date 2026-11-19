from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "A round speedometer points its bold needle into the last section of its scale."


def draw(s):
    angle = -24
    upright(s, oval(0, 40, 40, 40)[:-1], 7, 14, angle=angle)
    face = front_surface(s, angle=angle, y=7, z=40)
    face.oval(0, 0, 35, 35, DETAIL)
    for mark in range(225, -46, -45):
        a = radians(mark)
        face.line([(26*cos(a), 26*sin(a)), (31*cos(a), 31*sin(a))], EDGE)
    face.line(oval(0, 0, 27, 27, 0, -45, 12), EDGE)
    face.line([(1, -1), (22, -13)], BOLD)
    face.oval(0, 0, 3.5, 3.5, EDGE)
