from shapely.geometry import MultiPoint, Polygon

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._kit import badge
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "A water supply valve has its lever turned across the pipe and a slash badge on the valve body."


def draw(s):
    s.tube([(0, 5, 41), (0, 5, 23), (4, 5, 18), (67, 5, 18)], 4.3)
    along = lambda y, z: (66, y, z)
    s.face([along(y, z) for y, z in oval(5, 18, 6, 6, count=32)])
    printed_stroke(s, along, oval(5, 18, 3, 3, count=28), DETAIL)
    for x in (13, 51):
        hexagon = oval(5, 18, 6.5, 6.5, count=6)[:-1]
        near = [project((x, y, z)) for y, z in hexagon]
        far = [project((x - 5, y, z)) for y, z in hexagon]
        hull = MultiPoint(far + near).convex_hull
        s.layers.append((hull.boundary.union(Polygon(near).boundary), hull, EDGE))
    s.box(20, -4, 10, 23, 18, 16, 4)
    s.disk(31.5, 5, 26, 4.2, 4.2, 4.5)
    s.tube([(31.5, 5, 30.5), (31.5, 5, 35), (31.5, 28, 35)], 1.75)
    s.tube([(31.5, 23, 35), (31.5, 34, 35)], 2.5)
    badge(s, "slash", 41, 15.5, 16, 9.2)
