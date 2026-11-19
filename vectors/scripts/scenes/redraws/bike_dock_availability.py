from shapely.geometry import LineString
from shapely.ops import substring

from geometry import BOLD, EDGE, oval, project

DESCRIPTION = "A docking rack faces a dashed bicycle outline aligned with a vacant dock."


def draw(s):
    def dashed(points):
        path = LineString([project((x, 37 - x*.28, z)) for x, z in points])
        offset = 0
        while offset < path.length - 1:
            dash = substring(path, offset, min(offset + 3.8, path.length))
            s.layers.append((dash, None, BOLD))
            offset += 6.3

    for x in (14, 62):
        dashed(oval(x, 13, 13, 13, count=40))
    dashed([(14, 13), (30, 31), (36, 13), (14, 13)])
    dashed([(30, 31), (54, 29), (36, 13)])
    dashed([(62, 13), (54, 31), (52, 42), (58, 42)])
    dashed([(30, 31), (28, 39), (23, 39), (34, 39)])

    s.box(74, -26, 0, 15, 51, 3.5, 1.3)
    for y in (-23, -3, 17):
        s.box(76, y, 3, 9, 6, 27, 1.3)
        s.box(72, y, 23, 13, 6, 6, 1.3)
        s.line([(72, y + 1.5, 26), (72, y + 4.5, 26)], EDGE)
