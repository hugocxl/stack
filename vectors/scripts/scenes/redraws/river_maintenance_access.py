from math import pi, sin

from geometry import DETAIL, EDGE

DESCRIPTION = "A rail-lined maintenance ramp leads from the upper riverbank path down to the water's edge."


def draw(s):
    shoreline = [(-49, -1), (-30, 10), (-9, 13), (10, 20), (28, 17), (47, 10)]
    for x, y, length in ((-39, 24, 24), (-7, 31, 24), (21, 27, 24), (-23, 41, 24)):
        s.line([(x + length * i / 24, y + sin(i * pi / 8), 1) for i in range(25)], DETAIL)
    for a, b in zip(shoreline, shoreline[1:]):
        if a[0] == -9:
            continue
        s.face([(*a, 0), (*b, 0), (*b, 16), (*a, 16)], EDGE)
    s.face([(-49, -26, 16), (47, -26, 16), *[(*p, 16) for p in reversed(shoreline[3:])],
            (10, -9, 16), (-9, -9, 16), *[(*p, 16) for p in reversed(shoreline[:3])]], EDGE)
    s.line([(-43, -19, 16), (42, -19, 16)], DETAIL)
    ramp = [(-9, -9, 16), (10, -9, 16), (10, 26, 2), (-9, 26, 2)]
    s.face([(10, -9, 16), (10, 26, 2), (10, 26, 0), (10, -9, 14)], EDGE)
    s.face(ramp, EDGE)
    for x in (-9, 10):
        for y in (-7, 9, 24):
            z = 16 - (y + 9) * .4
            s.tube([(x, y, z), (x, y, z + 7)], .85, EDGE)
        s.tube([(x, -7, 22.2), (x, 24, 9.8)], 1, EDGE)
