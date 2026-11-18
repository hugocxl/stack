from math import cos, radians, sin

from shapely.geometry import MultiPoint, Polygon
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project

DESCRIPTION = "A ridged foam roller holds a broad loop of resistance band around one end."


def draw(s):
    def section(x, radius, start=0, end=360):
        return [(x, y, z) for y, z in oval(0, 24, radius, radius, start, end, count=48)]

    rear, front = -38, 39
    body = MultiPoint([project(p) for p in section(rear, 24) + section(front, 24)]).convex_hull
    bore = Polygon([project(p) for p in section(front, 13)])
    s.layers.append((body.boundary, body.difference(bore), EDGE))
    s.line(section(front, 24), EDGE)
    s.line(section(front, 13), EDGE)
    s.line(section(front - 6, 13, -42, 132), DETAIL)

    for angle in (-18, 12, 42, 72, 102):
        y, z = 24*cos(radians(angle)), 24+24*sin(radians(angle))
        s.line([(rear + 5, y, z), (front - 5, y, z)], DETAIL)

    # The lower run lies on the floor. The upper run climbs back onto the roller.
    low, high = 10, 23
    band = [(18, 8), (25, 4), (49, 3), (65, 5), (71, 9), (71, 13),
            (66, 17), (57, 19), (43, 23), (29, 29), (22, 35),
            (14, 43), (3, 48), (-9, 46), (-14, 44), (-17, 41)]
    ribbon = unary_union([
        Polygon([project(p) for p in ((low, y0, z0), (high, y0, z0),
                                     (high, y1, z1), (low, y1, z1))])
        for (y0, z0), (y1, z1) in zip(band, band[1:])
    ])
    s.layers.append((ribbon.boundary, ribbon, EDGE))
    s.line([(high, y, z) for y, z in band[4:]], DETAIL)
