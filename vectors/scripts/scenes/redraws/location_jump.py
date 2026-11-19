from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface, nav_path

DESCRIPTION = "A bent jump arrow runs across the folds of a map and points to a destination pin."


def draw(s):
    turn = radians(-23)
    c, q = cos(turn), sin(turn)
    folds = ((0, 15, 0), (32, -8, 5), (64, 18, 0), (96, -5, 5))
    height = 54
    paper_depth = 2.5

    def place(u, v):
        for left, right in zip(folds, folds[1:]):
            if u <= right[0]:
                start, depth, bottom = left
                end, next_depth, next_bottom = right
                mix = (u - start) / (end - start)
                y = depth + (next_depth - depth)*mix - .16*v
                z = paper_depth + bottom + (next_bottom - bottom)*mix + v
                return u*c - y*q, u*q + y*c, z
        raise ValueError("Point lies past the edge of the map")

    map_face = Surface(s, place)
    for (start, _, _), (end, _, _) in zip(folds, folds[1:]):
        map_face.slab([(start, 0), (end, 0), (end, height), (start, height)], paper_depth)

    map_face.line([(7, 41), (18, 47), (32, 40), (44, 40), (52, 48), (64, 44)], DETAIL)
    map_face.line([(18, 47), (16, 51)])
    map_face.line([(32, 40), (36, 32), (51, 34)])

    u, v = 80, 36
    map_face.outline([(u, v - 11), *oval(u, v + 3, 9, 9, -36, 216, count=32)], EDGE)
    map_face.oval(u, v + 3, 3.2, 3.2, EDGE)
    nav_path(map_face, [(12, 22), (28, 15), (32, 12), (64, 12),
                        (80, 12), (80, 22)], BOLD, head=7)
