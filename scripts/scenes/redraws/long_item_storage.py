from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project

DESCRIPTION = "A cantilever rack supports long pipes that extend beyond both sets of arms."


def draw(s):
    for y in (-24, 23):
        s.box(-19, y - 3, 0, 46, 6, 5, 1)
        s.box(-15, y - 3, 4, 6, 6, 53, 1)
        for z in (16, 35):
            s.box(-10, y - 3, z, 33, 6, 5, 1)
            s.box(20, y - 3, z + 5, 3, 6, 4, .4)
    s.box(-14, -24, 47, 4, 47, 5, .6)
    s.box(-14, -24, 10, 4, 47, 5, .6)

    for x, z, y in ((-3, 25.8, 38), (10, 25.8, 43),
                    (-3, 45.8, 45), (10, 45.8, 39), (3.5, 55.5, 42)):
        radius = 5.8
        rim = oval(x, z, radius, radius, count=32)[:-1]
        hull = MultiPoint([project((a, end, b)) for a, b in rim for end in (-44, y)]).convex_hull
        s.layers.append((hull.boundary, hull, EDGE))
        s.face([(a, y, b) for a, b in rim], EDGE)
        s.line([(a, y, b) for a, b in oval(x, z, radius - 2, radius - 2, count=28)], DETAIL)
