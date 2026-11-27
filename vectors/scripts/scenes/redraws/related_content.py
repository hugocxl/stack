from math import cos, radians, sin

from shapely.geometry import Polygon
from shapely.ops import unary_union

from geometry import BOLD, EDGE, interlace, project, rounded
from scenes.redraws._w4 import Surface, front_surface, landscape

DESCRIPTION = "Two staggered article cards are joined at their right edge by a pair of interlocked chain links."


def draw(s):
    angle = -7
    back = front_surface(s, angle=angle, y=-11, z=10, lean=.36)
    back.slab(rounded(8, 12, 78, 58, 5), 5)
    article = front_surface(s, angle=angle, y=0, z=10, lean=.36)
    article.slab(rounded(0, 0, 78, 58, 5), 5)
    article.rows(9, 49, (38,), ink=EDGE)
    photo = Surface(s, lambda u, v: article.at(9 + u, 38 - v))
    landscape(photo, 0, 0, 29, 27)
    article.rows(44, 35, (14, 12, 15, 12), step=-7)

    c, q = cos(radians(-10)), sin(radians(-10))

    def projected(points):
        return [project(article.at(77 + a*c - b*q, 33 + a*q + b*c)) for a, b in points]

    links = [
        Polygon(projected(rounded(u - 16, -8, 32, 16, 8)),
                [projected(rounded(u - 12, -4, 24, 8, 4))])
        for u in (-10, 10)
    ]
    half_planes = [
        Polygon(projected([(-40, 0), (40, 0), (40, v), (-40, v)]))
        for v in (-12, 12)
    ]
    interlace(s, links, [other.intersection(half) for other, half in zip(reversed(links), half_planes)], BOLD)
