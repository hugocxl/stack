from math import cos, pi, sin

from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A sloped museum panel displays a raised spiral fossil above a label with raised Braille dots."


def draw(s):
    s.box(22, 6, 0, 40, 26, 7, 3)
    s.box(29, 9, 7, 26, 16, 29, 2)
    face = Surface(s, (0, 45, 24), rise=(-.82, .57), back=(0, -.57, -.82))
    face.plate(rounded(0, 0, 85, 77, 4), 7)
    face.rect(7, 20, 71, 51, 3, DETAIL)
    align = face.viewer_axes(42, 45)

    def spiral_point(t, radius, depth):
        a = (t * 3.7 - .25) * pi
        return face.point(*align(radius * cos(a), radius * sin(a)), depth)

    for rib in range(10):
        t = .55 + rib * .047
        r = 3 + 17 * t
        s.line([spiral_point(t - .065, r - 8, -1.7),
                spiral_point(t - .034, r - 4, -2.5),
                spiral_point(t, r, -3)], EDGE)
    s.tube([spiral_point(i / 60, 3 + 17 * i / 60, -3)
            for i in range(61)], 1.7, BOLD)
    for x, cells in ((26, ((0, 0), (0, 1), (1, 2))),
                     (39, ((0, 0), (1, 0), (0, 1), (1, 2))),
                     (52, ((0, 0), (1, 0), (1, 1)))):
        for col, row in cells:
            u, v = x + col * 4.7, 14 - row * 4.1
            s.tube([face.point(u, v), face.point(u, v, -.8)], .9, EDGE)
