from math import cos, radians, sin

from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws._w5 import panel

DESCRIPTION = "Three wallet passes fan out behind a front pass with a house emblem."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.29, .96), back=(0, -.96, -.29))
    outline = rounded(0, 0, 88, 59, 5)
    pivot_x, pivot_v = 62, 13
    for angle, depth in ((-26, 11), (-13, 5)):
        theta = radians(angle)
        c, q = cos(theta), sin(theta)

        def point(u, v):
            x, h = u - pivot_x, v - pivot_v
            return face.point(pivot_x + c * x - q * h, pivot_v + q * x + c * h, depth)

        panel(s, outline, point, 4)
    face.plate(outline, 4)
    face.stroke([(15, 32), (31, 47), (47, 32)], EDGE)
    face.stroke([(20, 37), (20, 18), (42, 18), (42, 37)], EDGE)
    face.rect(28, 18, 7, 10, 1.2, EDGE)
    face.rules(54, 34, [22, 17], gap=8)
