from geometry import EDGE
from scenes.redraws._w4 import nav_window, raised_lens

DESCRIPTION = "A single magnifying glass overlaps a stepped stack of three browser windows."


def draw(s):
    nav_window(s, x=21, y=-6, z=30, width=96, height=60)
    nav_window(s, x=11, y=-3, z=15, width=96, height=60)
    face = nav_window(s, width=96, height=60)
    face.rows(12, 33, (29,), ink=EDGE)
    face.rows(12, 23, (38, 27), step=-8)
    raised_lens(face, 93, 37, 24, direction=(.91, -.42))
