from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._kit import badge
from scenes.redraws._w4 import bezier_path

DESCRIPTION = "A tailor's dress form wears a measuring tape and carries a clock badge by its shoulder."


def draw(s):
    s.disk(0, 0, 0, 19, 14, 4)
    s.disk(0, 0, 4, 3, 3, 24)
    contours = bezier_path(
        (27, 22, 12),
        ((34, 26, 14), (43, 23, 12), (49, 16, 9)),
        ((57, 13, 9), (59, 16, 11), (66, 20, 14)),
        ((73, 24, 14), (78, 24, 12), (82, 23, 10)),
        ((85, 19, 8), (86, 7, 6), (91, 6, 5)),
        count=9,
    )
    sections = [[(x, y, z) for x, y in oval(0, 0, rx, ry, count=48)[:-1]]
                for z, rx, ry in contours]
    projected = [[project(p) for p in ring] for ring in sections]
    shell = unary_union([MultiPoint(a + b).convex_hull for a, b in zip(projected, projected[1:])])
    s.layers.append((shell.boundary, shell, EDGE))
    s.line([(x, y, 27) for x, y in oval(0, 0, 22, 12, 0, 90)], DETAIL)
    s.line([(rx*.39, ry*.92, z) for z, rx, ry in contours], DETAIL)
    long_end = bezier_path(
        (-4, 6, 89),
        ((-5, 8, 84), (-11, 10, 83), (-11, 12, 76)),
        ((-12, 13, 68), (-6, 11, 63), (-2, 10, 56)),
        count=6,
    )
    short_end = bezier_path(
        (4, 6, 89),
        ((6, 8, 85), (12, 10, 84), (12, 12, 77)),
        ((12, 13, 74), (11, 13, 71), (10, 13, 68)),
        count=6,
    )
    for tape in (long_end, short_end):
        other_edge = [(x + 3.6, y, z - .7) for x, y, z in tape]
        s.face([*tape, *reversed(other_edge)])
        for (x, y, z), (a, b, c) in zip(tape[3:-1:2], other_edge[3:-1:2]):
            s.line([(x, y, z), ((x + a)/2, (y + b)/2, (z + c)/2)], DETAIL)
    s.disk(0, 0, 90, 6.3, 5.3, 4)
    badge(s, "clock", 25, -7, 82, 13)
