from math import cos, sin, tau

from shapely.geometry import Polygon
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, project

DESCRIPTION = "A measuring tape follows the curved seam of a contoured pillow."


def draw(s):
    # Loft a pillow with rounded corners and a shallow trough between its two lobes.
    sections = ((0, 22, .10), (3, 28, .46), (9, 32, .81), (17, 34, .98),
                (28, 34.5, 1), (44, 34.5, 1), (62, 34.5, 1), (78, 34.5, 1),
                (90, 33, .90), (97, 30, .62), (101, 23, .17))

    def section(x, width, loft):
        for i in range(48):
            angle = tau*i/48
            side, rise = cos(angle), sin(angle)
            contour = rise * (10 + 24*side**2) if rise > 0 else 11*rise
            yield x, 35 + width*side, 12 + loft*contour

    rings = [[project(p) for p in section(*dimensions)] for dimensions in sections]
    patches = [Polygon(rings[0]), Polygon(rings[-1])]
    for back, front in zip(rings, rings[1:]):
        for i in range(len(front)):
            patch = Polygon((back[i - 1], back[i], front[i], front[i - 1]))
            if patch.is_valid and patch.area > .001:
                patches.append(patch)
    pillow = unary_union(patches)
    s.layers.append((pillow.boundary, pillow, EDGE))

    s.line([(x, 35, 12 + loft*10) for x, _, loft in sections[1:-1]], DETAIL)
    s.line([(x, 35 + width, 12) for x, width, _ in sections[1:]], DETAIL)
    s.line([(101, 35 + 23*cos(tau*i/48), 12) for i in range(25)], DETAIL)

    # The ticked tape hugs the near lobe, then drops off the corner.
    path = [(18, 69.5, 13), (33, 70, 14), (49, 70, 15), (65, 70, 15),
            (80, 70, 14), (92, 68, 12), (102, 65, 8), (110, 64, 4)]
    top = [(x, y, z + 3.5) for x, y, z in path]
    bottom = [(x, y, z - 3.5) for x, y, z in path]
    s.face([*top, *reversed(bottom)], EDGE)
    for (x, y, z), (a, b, c) in zip(path, path[1:]):
        for t in (.30, .63):
            px, py, pz = x + t*(a - x), y + t*(b - y), z + t*(c - z)
            s.line([(px, py, pz + 3.5), (px, py, pz + (0 if t < .5 else -1))], EDGE)
