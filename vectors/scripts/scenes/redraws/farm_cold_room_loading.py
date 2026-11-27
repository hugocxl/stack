from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._sf import plane, plate, squircle
from scenes.redraws._w5 import harvest_crate

DESCRIPTION = "A produce crate waits at the open door of a walk-in cooler marked with a snowflake."


def snowflake(s, y, z, r, x):
    for a in (90, 30, 150):
        dy, dz = r*cos(radians(a)), r*sin(radians(a))
        s.line([(x, y - dy, z - dz), (x, y + dy, z + dz)], EDGE)


def draw(s):
    W, D, H = 72, 46, 64
    d0, d1, top = 10, 46, 56
    # The interior seen through the doorway: back floor edge and the far corner.
    s.line([(d0, 8, 3), (d1, 8, 3)], DETAIL)
    s.line([(d0, 8, 3), (d0, 8, top)], DETAIL)
    s.line([(d0, 8, 3), (d0, D, 3)], DETAIL)
    s.face([(0, 0, H), (W, 0, H), (W, D, H), (0, D, H)], EDGE)
    s.face([(W, 0, 0), (W, D, 0), (W, D, H), (W, 0, H)], EDGE)
    s.face([(0, D, 0), (W, D, 0), (W, D, H), (0, D, H)], EDGE,
           openings=[[(d0, D, 3), (d1, D, 3), (d1, D, top), (d0, D, top)]])
    s.line([(d0 - 3, D, 0), (d0 - 3, D, top + 3), (d1 + 3, D, top + 3), (d1 + 3, D, 0)], DETAIL)
    snowflake(s, D/2, 38, 10, W)
    # The insulated door stands open toward the viewer on its left hinge.
    leaf = plane((d0 - 1, D + 1, 1), (-.26, .97, 0), (0, 0, 1))
    plate(s, leaf, squircle(d1 - d0, top - 1, 3), 6, (-.97, -.26, 0))
    s.tube([leaf(d1 - d0 - 6, 22), leaf(d1 - d0 - 6, 36)], 1.4, EDGE)
    harvest_crate(s, 10, 52, 0, scale=.62)
