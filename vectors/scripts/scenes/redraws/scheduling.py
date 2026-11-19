from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w2 import closed_outline, upright_face

DESCRIPTION = "Two long appointment blocks span cells on different rows of a ring-bound desk calendar."


def draw(s):
    def point(x, v):
        return .52*x, -.48*x - .48*v, .87*v

    width, height = 110, 91
    left, right = point(0, height), point(width, height)
    s.face([(0, -69, 0), (.52*width, -.48*width - 69, 0), right, left], EDGE)
    upright_face(s, point, rounded(0, 0, width, height, 4), 4)
    for x in (23, 86):
        a, b, z = point(x, 87)
        s.tube([(a, y, c) for y, c in oval(b - 2, z + 4, 4.8, 8, -65, 230, 24)], 1.5)

    closed_outline(s, point, [(9, 9), (101, 9), (101, 70), (9, 70)], DETAIL)
    for x in (32, 55, 78):
        s.line([point(x, 9), point(x, 70)], DETAIL)
    for v in (30, 50):
        s.line([point(9, v), point(101, v)], DETAIL)

    for x, v, length in ((12, 54, 40), (35, 13, 63)):
        upright_face(s, point, rounded(x, v, length, 13, 3), 2.5, EDGE)
        s.line([point(x + 6, v + 6.5), point(x + 16, v + 6.5)], DETAIL)
