from math import cos, radians, sin

from geometry import EDGE
from scenes.redraws._sf import house

DESCRIPTION = "A circular arrow orbits a small house on the ground, a full turn around the property."


def draw(s):
    R = 64
    ring = [(R*cos(radians(a)), R*sin(radians(a)), 0) for a in range(-150, 181, 5)]
    back = [p for p in ring if p[0] + p[1] < 0]
    front = [p for p in ring if p[0] + p[1] >= 0]
    s.line(back, EDGE)
    house(s, -26, -22, 0, 52, 44, 30, 22)
    s.line(front, EDGE)
    a = radians(180)
    tip = (R*cos(a), R*sin(a), 0)
    s.line([(tip[0] + 7, tip[1] + 9, 0), tip, (tip[0] - 7, tip[1] + 9, 0)], EDGE)
