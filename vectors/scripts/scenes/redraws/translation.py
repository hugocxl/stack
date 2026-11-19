from geometry import EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_line, rule, upright_face

DESCRIPTION = "Two thick text panels show distinct writing patterns with exchange arrows between them."


def draw(s):
    def left(x, z):
        return .82*x, -.18*x - .17*z, z

    def right(x, z):
        return 82 + .63*x, -22 - .37*x - .17*z, z + 1

    outline = rounded(0, 0, 50, 59, 5)
    upright_face(s, right, outline, 6)
    upright_face(s, left, outline, 6)
    for z in (43, 29, 15):
        for x, length in ((8, 10), (22, 6), (32, 8)):
            rule(s, left, x, z, length, EDGE)

    for z in (42, 20):
        for x in (10, 28):
            chart_line(s, right, [(x, z), (x + 10, z), (x + 10, z - 10),
                                  (x, z - 10), (x, z)], EDGE)
            chart_line(s, right, [(x, z - 4), (x + 10, z - 7)], EDGE)
    arrow(s, [(47, -15, 47), (78, -23, 47)], head=8)
    arrow(s, [(77, -23, 28), (47, -15, 28)], head=8)
