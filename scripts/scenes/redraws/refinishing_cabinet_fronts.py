from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, upright_face

DESCRIPTION = "A finishing roller leaves a straight strip along one side of a cabinet door with a raised frame and pull handle."


def draw(s):
    def p(x, z):
        return .86*x, -.14*x - .27*z, .91*z

    upright_face(s, p, rounded(0, 0, 66, 94, 2), 7)
    closed_outline(s, p, rounded(7, 7, 52, 80, 2), DETAIL)
    x, y, z = p(14, 48)
    s.tube([(x, y, z - 10), (x, y + 4, z - 9), (x, y + 4, z + 9),
            (x, y, z + 10)], 1.6, EDGE)

    s.line([p(32, 65), p(32, 17), p(49, 17), p(49, 65)], EDGE)
    s.line([p(37, 22), p(37, 44)], DETAIL)
    s.line([p(43, 31), p(43, 48)], DETAIL)
    left, right = p(30, 65), p(50, 65)
    s.tube([(left[0], left[1] + 2, left[2]), (right[0], right[1] + 2, right[2])], 3.2)
    a, b, c = right
    s.line([(a + 3, b + 2, c), (a + 7, b + 2, c), (a + 7, b + 2, c - 7),
            (a - 2, b + 2, c - 10), (a - 2, b + 2, c - 14)], EDGE)
    s.tube([(a - 2, b + 2, c - 14), (a - 2, b + 2, c - 24)], 2.3)
