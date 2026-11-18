from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, project, rounded
from scenes.redraws._w2 import chart_marker, rule

DESCRIPTION = "An instant photograph has a callout label pointing to the sailboat outlined inside it."


def draw(s):
    def p(x, z):
        return x, -.16*z, z

    front = [p(x, z) for x, z in rounded(0, 0, 94, 85, 4)]
    back = [(x, y - 6, z) for x, y, z in front]
    hull = MultiPoint([project(a) for a in front + back]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(front + front[:1], EDGE)
    s.face([p(8, 16), p(86, 16), p(86, 77), p(8, 77)], DETAIL)
    # Broad hull, mast, and sail leave room for the annotation to land.
    hull = [(21, 31), (68, 31), (60, 23), (29, 23), (21, 31)]
    sail = [(43, 35), (44, 66), (64, 35), (43, 35)]
    for shape in (hull, sail):
        s.line([p(x, z) for x, z in shape], EDGE)
    s.line([p(41, 32), p(41, 64)], DETAIL)
    chart_marker(s, p, 55, 49, 1.7, BOLD)
    s.line([p(56, 49), p(70, 59), p(83, 59)], EDGE)
    s.face([p(x, z) for x, z in rounded(82, 50, 44, 21, 4)], BOLD)
    rule(s, p, 90, 63, 26, EDGE)
    rule(s, p, 90, 57, 17, DETAIL)
