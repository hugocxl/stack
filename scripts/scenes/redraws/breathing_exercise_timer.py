from math import cos, pi, radians, sin

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "An hourglass breathing timer carries a broad airflow wave across its upper bulb."


def draw(s):
    angle = -36
    profile = [(-25, 6), (-27, 21), (-25, 30), (-19, 39), (-10, 47),
               (-5, 51), (-5, 56), (-10, 61), (-20, 70), (-26, 80),
               (-27, 87), (-25, 95), (25, 95), (27, 87), (26, 80),
               (20, 70), (10, 61), (5, 56), (5, 51), (10, 47), (19, 39),
               (25, 30), (27, 21), (25, 6)]
    upright(s, profile, 3, 7, angle=angle)
    c, q = cos(radians(angle)), sin(radians(angle))
    foot = [(u*c - v*q, u*q + v*c) for u, v in oval(0, 0, 31, 17)[:-1]]
    s.solid(foot, 0, 6)
    s.solid(foot, 94, 7)

    glass = front_surface(s, angle=angle, y=3)
    glass.line([(0, 49), (0, 34)], DETAIL, dashed=True)
    glass.line([(-18, 24), (-10, 26), (-4, 30), (0, 31),
                (4, 30), (10, 26), (18, 24)], EDGE)
    glass.line([(u, 76 + 4.2*sin(pi*u/14)) for u in range(-19, 20)], BOLD)
