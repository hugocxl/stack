from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A tall thermometer rises above a cluster of city rooftops."


def building(s, x, y, width, depth, height, windows):
    s.box(x, y, 0, width, depth, height, 1.3)
    for column in range(windows):
        left = x + 4 + column * 9
        for z in range(9, height - 8, 12):
            s.line([(left, y + depth, z), (left, y + depth, z + 5),
                    (left + 4, y + depth, z + 5), (left + 4, y + depth, z)], DETAIL)


def draw(s):
    building(s, -16, -16, 26, 23, 59, 2)
    building(s, -38, -3, 23, 23, 39, 2)
    building(s, -12, 11, 25, 21, 30, 2)

    x, y, bulb = 28, 13, 28
    bottom = oval(x, bulb, 13, 13, 117, 423, 38)
    cap = oval(x, 83, 6, 6, 0, 180, 18)
    upright_profile(s, list(reversed(bottom + cap)), y, 4)
    s.line([(a, y, b) for a, b in oval(x, bulb, 7, 7, count=32)], BOLD)
    s.line([(x, y, bulb + 7), (x, y, 74)], BOLD)
    for z in (47, 56, 65, 74):
        s.line([(x + 2.5, y, z), (x + 4.4, y, z)], EDGE)
