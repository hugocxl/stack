from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._w2 import closed_outline, printed_glyph, rule, upright_face

DESCRIPTION = "A pushpin pierces the upper edge of a square decision note with a large checked box."


def draw(s):
    def point(x, z):
        return .72*x, -.28*x - .22*z, .9*z

    upright_face(s, point, rounded(0, 0, 84, 84, 2), 3)
    closed_outline(s, point, [(14, 34), (37, 34), (37, 57), (14, 57)], EDGE)
    printed_glyph(s, point, "check", 26, 46, 11, BOLD)
    rule(s, point, 47, 51, 22, EDGE)
    rule(s, point, 47, 40, 17, DETAIL)
    rule(s, point, 14, 21, 53, DETAIL)

    def ring(offset, radius):
        return [(a + offset, b + offset, c + offset*2.9)
                for x, z in oval(38, 71, radius, radius)
                for a, b, c in (point(x, z),)]

    def section(back, front):
        hull = MultiPoint([project(p) for p in back + front]).convex_hull
        s.layers.append((hull.boundary, hull, EDGE))

    a, b, c = point(38, 71)
    s.tube([(a, b, c), (a + 2, b + 2, c + 6)], .8, EDGE)
    section(ring(1.6, 8), ring(2.7, 8))
    section(ring(2.7, 4.1), ring(6.3, 4.1))
    head = ring(7.5, 10)
    section(ring(6.3, 9.5), head)
    s.face(head, EDGE)
