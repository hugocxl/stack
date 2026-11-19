from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, oval, project

DESCRIPTION = "A round water meter with a pointer dial is fitted inline between two pipe couplings."


def coupling(s, start, end, radius):
    """Draw a sleeve around the horizontal pipe."""
    profile = oval(0, 10, radius, radius, count=36)
    front = [(end, y, z) for y, z in profile]
    points = [project((x, y, z)) for x in (start, end) for y, z in profile]
    hull = MultiPoint(points).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(front, EDGE)


def draw(s):
    s.tube([(-48, 0, 10), (48, 0, 10)], 4.1, EDGE)
    coupling(s, -37, -24, 7.2)
    s.disk(0, 0, 0, 21, 17, 17, EDGE)
    coupling(s, 22, 34, 7.2)
    s.disk(0, 0, 15, 16, 16, 10, EDGE)
    s.disk(0, 0, 23, 19, 19, 4, EDGE)
    s.ellipse(0, 0, 27, 15, 15, EDGE)
    for x, y in oval(0, 0, 12, 12, 150, 360, 5):
        s.line([(x, y, 27), (x*.78, y*.78, 27)], DETAIL)
    s.line([(-2, 2, 27), (0, 0, 27), (8, -7, 27)], BOLD)
