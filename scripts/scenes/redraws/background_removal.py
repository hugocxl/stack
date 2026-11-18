from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, upright_face

DESCRIPTION = "A pear cutout stands forward from an exposed checkerboard transparency field."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x - .25*z, z

    upright_face(s, point, rounded(0, 0, 89, 72, 4), 7)
    for row in range(4):
        for col in range(5):
            if (row + col) % 2 == 0:
                x, z = 7 + 15*col, 7 + 14*row
                s.face([point(u, v) for u, v in rounded(x, z, 15, 14, .3)], DETAIL)

    def cutout(x, z):
        a, b, c = point(x, z)
        return a - 3, b + 19, c + 34

    pear = [(43, 12), (33, 13), (25, 17), (20, 24), (20, 32), (23, 39),
            (31, 47), (34, 54), (39, 58), (46, 58), (52, 54), (54, 46),
            (61, 39), (65, 31), (64, 23), (59, 17), (52, 13)]
    curve = []
    for i, (x, z) in enumerate(pear):
        x0, z0 = pear[i - 1]
        x2, z2 = pear[(i + 1) % len(pear)]
        for j in range(5):
            t = j/5
            curve.append(((1 - t)**2 * (x0 + x)/2 + 2*t*(1 - t)*x + t*t*(x + x2)/2,
                          (1 - t)**2 * (z0 + z)/2 + 2*t*(1 - t)*z + t*t*(z + z2)/2))
    s.face([cutout(x, z) for x, z in curve], BOLD)
    chart_line(s, cutout, [(44, 57), (45, 65), (50, 71)], EDGE)
    s.face([cutout(x, z) for x, z in
            [(45, 65), (53, 70), (63, 72), (58, 65), (52, 62)]], EDGE)
