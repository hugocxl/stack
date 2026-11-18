from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, project, rounded
from scenes.redraws._w2 import chart_marker

DESCRIPTION = "A calculator shows a dot addition problem and its three-dot result above a bank of keys."


def draw(s):
    def point(x, v):
        return x*.55, -x*.45 - v*.71, 7 + v*.45

    front = [point(x, v) for x, v in rounded(0, 0, 73, 92, 5)]
    back = [(x, y - 2, z - 7) for x, y, z in front]
    hull = MultiPoint([project(vertex) for vertex in front + back]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(front + front[:1], EDGE)
    s.face([point(x, v) for x, v in rounded(9, 53, 55, 30, 3)])
    for v in (12, 25, 38):
        for x in (10, 29, 48):
            s.face([point(u, w) for u, w in rounded(x, v, 14, 8, 2)], DETAIL)
    for x, v in ((22, 74), (42, 74), (51, 74), (36, 62), (45, 62), (54, 62)):
        chart_marker(s, point, x, v, 2.5, EDGE)
    s.line([point(29, 74), point(35, 74)], BOLD)
    s.line([point(32, 71), point(32, 77)], BOLD)
    s.line([point(20, 60), point(27, 60)], EDGE)
    s.line([point(20, 64), point(27, 64)], EDGE)
