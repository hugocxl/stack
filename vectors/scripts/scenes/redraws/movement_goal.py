from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import BACK, plate, screen, smooth
from scenes.redraws.approval_rate import band

DESCRIPTION = "A thick step-goal ring, mostly complete, surrounds a single footprint."


def draw(s):
    at = screen()
    s.line([at(44*cos(radians(a)), 44*sin(radians(a))) for a in range(0, 361, 3)], DETAIL)
    plate(s, at, band(-200, 90, 44, 14), 7, BACK)
    sole = smooth([(0, -20), (9, -14), (10, 2), (7, 12), (0, 14), (-7, 10), (-9, -2), (-8, -14)], 4, closed=True)
    s.line([at(u, v - 4) for u, v in sole] + [at(sole[0][0], sole[0][1] - 4)], EDGE)
    for u, v, r in ((-6, 15, 2.6), (-1, 18, 2.4), (4, 18, 2.2), (8, 15.5, 2), (10.5, 11.5, 1.8)):
        s.line([at(u + a, v + b) for a, b in oval(0, 0, r, r, count=16)], EDGE)
