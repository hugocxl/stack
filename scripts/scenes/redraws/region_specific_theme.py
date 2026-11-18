from math import cos, radians, sin

from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Three theme swatch strips fan out from a shared rivet set inside a map-pin clasp."


def draw(s):
    for angle, depth in ((-34, 10), (0, 6), (34, 2)):
        a = radians(angle)
        strip = Surface(s, (0, -depth, 24), rise=(-.25, .97), across=(.98, -.18))

        def turn(x, v):
            return (x * cos(a) - v * sin(a), x * sin(a) + v * cos(a))

        strip.plate([turn(x, v) for x, v in rounded(-12, -19, 24, 102, 5)], 4)
        for v in (23, 44, 65):
            strip.stroke([turn(x, h) for x, h in rounded(-7, v, 14, 13, 2)],
                         EDGE, closed=True)

    # The clasp is the fastener itself, with its rivet visible through the center.
    clasp = Surface(s, strip.point(0, 0, -3), across=strip.across)
    place = clasp.viewer_axes(0, 0)
    pin = [*oval(0, 0, 11, 11, -38, 218, 32), (0, -22)]
    clasp.plate([place(u, v) for u, v in pin], 3, BOLD)
    clasp.stroke([place(u, v) for u, v in oval(0, 0, 4.4, 4.4)], EDGE)
