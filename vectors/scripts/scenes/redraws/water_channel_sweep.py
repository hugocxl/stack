from math import sin

from geometry import DETAIL, EDGE
from scenes.redraws._sf import plane, plate

DESCRIPTION = "Water flows along an open concrete channel, carrying two leaves downstream past a flow arrow."


def draw(s):
    L = 130
    profile = [(0, 0), (40, 0), (40, 18), (32, 18), (30, 6), (10, 6), (8, 18), (0, 18)]
    end = plane((-L/2, 20, 0), (0, -1, 0), (0, 0, 1))
    plate(s, end, profile, L, (1, 0, 0))
    for y in (2, 9, 16):
        s.line([(-L/2 + 6 + t, y - 20 + 20, 12 + .8*sin(t/6)) for t in range(0, L - 10, 3)], DETAIL)
    for x, y in ((-20, 4), (24, 12)):
        s.face([(x - 5, y, 12.5), (x, y - 3, 12.5), (x + 6, y, 12.5), (x, y + 3, 12.5)], EDGE)
    s.line([(40, 10, 13), (56, 10, 13)], EDGE)
    s.line([(51, 6, 13), (56, 10, 13), (51, 14, 13)], EDGE)
