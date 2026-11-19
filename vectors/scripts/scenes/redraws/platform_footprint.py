from math import cos, radians, sin

from geometry import BOLD, DETAIL
from scenes.redraws._w4 import Surface

DESCRIPTION = "An upright folded map outlines a single deployment district across its folds."


def folded_map(s):
    panels = []
    folds = ((0, 0), (31, 13), (61, -3), (93, 10))
    c, q = cos(radians(-26)), sin(radians(-26))
    for (u0, y0), (u1, y1) in zip(folds, folds[1:]):
        def place(u, z, u0=u0, u1=u1, y0=y0, y1=y1):
            y = y0 + (u - u0) * (y1 - y0) / (u1 - u0)
            return u*c - y*q, u*q + y*c, z

        panel = Surface(s, place)
        panel.slab([(u0, 3), (u1, 3), (u1, 67), (u0, 67)], 3)
        panels.append(panel)
    return panels


def draw(s):
    west, center, east = folded_map(s)
    west.line([(0, 23), (13, 25), (22, 15), (31, 15)], DETAIL)
    center.line([(31, 15), (44, 13), (57, 20), (61, 19)], DETAIL)
    east.line([(61, 19), (73, 16), (83, 25), (93, 22)], DETAIL)
    west.line([(31, 50), (20, 54), (11, 43), (20, 30), (31, 27)], BOLD)
    center.line([(31, 50), (45, 57), (55, 49), (61, 49)], BOLD)
    center.line([(31, 27), (43, 31), (55, 27), (61, 32)], BOLD)
    east.line([(61, 49), (75, 47), (82, 37), (69, 32), (61, 32)], BOLD)
