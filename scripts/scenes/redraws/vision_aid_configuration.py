from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A pair of adjustable eyeglasses has a bridge with calibration ticks between its two lenses."


def draw(s):
    plane = front_surface(s, angle=-26, z=10)
    point = plane.at
    for hinge, tip in ((2, 10), (104, 94)):
        x, y, z = point(hinge, 26)
        a, b, c = point(tip, 1)
        s.tube([(x, y, z), (x-9, y-14, z), (a-32, b-55, c+17),
                (a-34, b-62, c+10)], 1.9)

    for u in (0, 63):
        outer = rounded(u, 0, 43, 34, 13)
        inner = rounded(u + 3, 3, 37, 28, 10)
        s.face([point(a, b) for a, b in outer],
               openings=[[point(a, b) for a, b in inner]])
        plane.line([(u + 3, 25), (u + 7, 30)], DETAIL)
    plane.frame(42, 19, 22, 13, 2, BOLD)
    for index, u in enumerate((46, 49.5, 53, 56.5, 60)):
        plane.line([(u, 22), (u, 28 if index == 2 else 26)], EDGE)
