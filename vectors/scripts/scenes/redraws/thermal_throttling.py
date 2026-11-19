from math import acos, degrees

from geometry import BOLD, EDGE, oval
from scenes.systems_shapes import rectangle

DESCRIPTION = "A processor shows three descending performance bars beside a thermometer."


def draw(s):
    for x in range(-30, 31, 12):
        s.box(x - 2, 25, 0, 4, 8, 2, 1.5)
    for y in range(-17, 18, 11):
        s.box(36, y - 2, 0, 8, 4, 2, 1.5)
    s.box(-39, -27, 0, 78, 54, 8, 4)
    rectangle(s, -33, -21, 8, 66, 42, radius=2)
    for x, height in ((-28, 29), (-11, 21), (6, 11)):
        rectangle(s, x, 10 - height, 8, 10, height, EDGE, 1)

    # The bulb and stem share a continuous outline.
    x, y, z = 36, 17, 13
    bulb, stem = 8, 3.6
    join_angle = degrees(acos(stem / bulb))
    arc = oval(x, z, bulb, bulb, 180 - join_angle, 360 + join_angle, 36)
    neck = [(a, y, b) for a, b in oval(x, 38, stem, stem, 0, 180, 16)]
    s.face([(a, y, b) for a, b in arc] + neck, EDGE)
    s.line([(x, y, z), (x, y, 32)], BOLD)
