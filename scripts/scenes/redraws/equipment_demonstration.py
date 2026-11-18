from math import hypot

from shapely.geometry import MultiPoint

from geometry import BOLD, EDGE, oval, project
from scenes.redraws._w3 import Surface, flat

DESCRIPTION = "A specimen slide rests halfway onto the stage of a benchtop microscope."


def optical_tube(s, bottom, top, radius, ink=EDGE):
    """A tilted cylindrical barrel with a visible circular opening at its upper end."""
    dx, dz = top[0] - bottom[0], top[2] - bottom[2]
    length = hypot(dx, dz)

    def rim(center, r):
        x, y, z = center
        return [(x + u * dz / length, y + v, z - u * dx / length)
                for u, v in oval(0, 0, r, r, count=48)[:-1]]

    front = rim(top, radius)
    hull = MultiPoint([project(p) for p in rim(bottom, radius) + front]).convex_hull
    s.layers.append((hull.boundary, hull, ink))
    s.face(front, ink)
    opening = rim(top, radius * .63)
    s.line([*opening, opening[0]], EDGE)


def draw(s):
    s.box(3, 4, 0, 76, 58, 8, 10)
    arm = Surface(s, (0, 26, 0))
    arm.plate([(10, 7), (28, 7), (21, 23), (19, 50), (24, 67),
               (36, 77), (51, 80), (49, 92), (32, 92), (15, 83),
               (8, 68), (5, 49), (6, 26)], 15)
    s.disk(43, 30, 8, 10, 10, 9)
    s.box(24, 8, 34, 47, 38, 5, 3)
    flat(s, 0, 46, 39).rect(39, 11, 17, 15, 3)
    s.disk(46, 24, 49, 7, 7, 9)
    s.disk(46, 24, 58, 12.5, 11, 7)
    optical_tube(s, (46, 24, 64), (53, 24, 91), 11)
    optical_tube(s, (52, 24, 89), (55, 24, 100), 14, BOLD)
    arm.oval(18, 51, 9, 9, EDGE)
    arm.oval(18, 51, 5, 5)
    slide = flat(s, 0, 48, 41)
    slide.plate([(38, 11), (86, 11), (86, 23), (38, 23)], 1)
    slide.oval(50, 17, 4, 4, EDGE)
