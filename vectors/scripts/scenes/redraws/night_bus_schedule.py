from math import sqrt

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws.bus_shelter_directory import bus_pictogram

DESCRIPTION = "A framed bus timetable has four departure rows under a crescent-moon emblem."


def draw(s):
    s.box(4, -7, 0, 45, 13, 4, 2)
    s.box(7, -4, 4, 3, 5, 11, 1)
    s.box(43, -4, 4, 3, 5, 11, 1)
    s.box(0, -3, 11, 53, 5, 58, 3)
    bus_pictogram(s, 15, 2, 54, 1.02)
    s.line([(5, 2, 40), (48, 2, 40)], EDGE)
    for z in (33, 27, 21, 15):
        s.line([(8, 2, z), (16, 2, z)], DETAIL)
        s.line([(23, 2, z), (43, 2, z)], DETAIL)

    x, y, z = 37, 2, 55
    outer = oval(x, z, 9, 9, 63, 308, 42)
    inner = [(41.1 - sqrt(8.6 ** 2 - (b - 55) ** 2), b)
             for b in [outer[-1][1] + (outer[0][1] - outer[-1][1]) * i / 24 for i in range(25)]]
    s.face([(a, y, b) for a, b in outer + inner], BOLD)
