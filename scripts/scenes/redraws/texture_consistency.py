from math import pi, sin

from geometry import EDGE
from scenes.redraws._w2 import chart_line, upright_face

DESCRIPTION = "A folded material swatch carries the same flowing grain across both sides of its seam."


def draw(s):
    def left(x, z):
        return .91*x, -.09*x - .32*z, z

    def right(x, z):
        return 44.59 + .34*x, -4.41 - .66*x - .32*z, z

    panel = [(0, 0), (49, 0), (49, 68), (0, 68)]
    upright_face(s, right, panel, 7)
    upright_face(s, left, panel, 7)
    for level in (10, 22, 34, 46, 58):
        def grain(x):
            return level + 3.3*sin(x*pi/26 + level*.02) + 1.1*sin(x*pi/13)

        chart_line(s, left, [(x, grain(x)) for x in range(4, 50, 3)], EDGE)
        chart_line(s, right, [(x, grain(49 + x)) for x in range(0, 46, 3)], EDGE)
