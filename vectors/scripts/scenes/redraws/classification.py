from geometry import EDGE, oval
from scenes.redraws._w2 import chart_line, upright_face

DESCRIPTION = "A single input branches into three category bins marked with a circle, triangle, and square."


def draw(s):
    def point(x, z):
        return .64*x, -.36*x, z

    def bin_(x, z, outline):
        upright_face(s, lambda u, v: point(u + x, v + z), outline, 5)

    chart_line(s, point, [(56, 66), (56, 46), (17, 46), (17, 24)], EDGE)
    chart_line(s, point, [(56, 46), (56, 26)], EDGE)
    chart_line(s, point, [(56, 46), (95, 46), (95, 24)], EDGE)
    bin_(56, 72, [(0, 12), (15, 4), (15, -5), (0, -13),
                  (-15, -5), (-15, 4)])
    bin_(17, 16, oval(0, 0, 12, 12, count=36)[:-1])
    bin_(56, 15, [(-13, -11), (13, -11), (0, 14)])
    bin_(95, 16, [(-11, -11), (11, -11), (11, 11), (-11, 11)])
