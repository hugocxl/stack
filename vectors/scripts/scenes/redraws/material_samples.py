from math import cos, radians, sin

from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project, rounded

DESCRIPTION = "Three textured material samples fan out from a shared binding rivet."


def swatch_fan(s, *, paint=False):
    """Draw three rigid sample chips around a common pivot, with their ends spread."""
    width, length = (23, 65) if paint else (28, 72)
    angles = (52, 16, -20) if paint else (60, 20, -21)
    for index, degrees in enumerate(angles):
        angle = radians(degrees)
        depth = (2 if paint else 3.2) * index

        def point(u, v, layer=0):
            across = u * cos(angle) - v * sin(angle)
            up = u * sin(angle) + v * cos(angle)
            offset = depth + layer
            return (
                .707 * across - .44 * up + .707 * offset,
                -.707 * across - .44 * up + .707 * offset,
                15 + .78 * up,
            )

        edge = rounded(-width / 2, -12, width, length + 12, 4)
        front = [point(u, v) for u, v in edge]
        back = [point(u, v, -1.6 if paint else -2.7) for u, v in edge]
        hull = MultiPoint([project(p) for p in front + back]).convex_hull
        s.layers.append((hull.boundary, hull, EDGE))
        s.line(front + front[:1], EDGE)

        if paint:
            for v in (26, 43):
                s.line([point(-width / 2, v), point(width / 2, v)], DETAIL)
        elif index == 0:
            # Tangential grain on the timber chip.
            for u, top in ((-8, 62), (0, 67), (8, 65)):
                s.line([point(u, top - 29), point(u + 2, top - 19),
                        point(u - 2, top - 9), point(u, top)], DETAIL)
        elif index == 1:
            # Scattered aggregates in a stone composite.
            for u, v, r in ((-8, 62, 1.3), (2, 60, 2), (8, 66, 1.4),
                            (-3, 53, 1.8), (7, 48, 1.4), (-8, 45, 1.1),
                            (1, 39, 1.7), (7, 33, 1.2)):
                s.line([point(a, b) for a, b in oval(u, v, r, r * .73, count=16)], DETAIL)
        else:
            # Broad crossing strands in the woven chip.
            for u in (-8, 0, 8):
                s.line([point(u, 30), point(u, 65)], DETAIL)
            for v in (36, 46, 56, 63):
                s.line([point(-10, v), point(10, v)], DETAIL)

    s.line([point(u, v) for u, v in oval(0, 0, 3.9, 3.9)], EDGE)
    return point


def draw(s):
    swatch_fan(s)
