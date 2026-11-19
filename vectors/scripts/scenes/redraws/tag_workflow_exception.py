from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import warning
from scenes.redraws._w2 import chart_line, closed_outline, upright_face

DESCRIPTION = "A warning triangle clips to the edge of a looped workflow tag with a three-step route."


def draw(s):
    def point(x, z):
        return .70*x, -.30*x - .18*z, .96*z

    tag = [(0, 0), (80, 0), (105, 26), (105, 42), (80, 68), (0, 68)]
    s.tube([point(x, z) for x, z in ((120, 42), (122, 37), (118, 30),
                                     (111, 28), (103, 30), (92, 34))], 1.5, EDGE)
    upright_face(s, point, tag, 6)
    closed_outline(s, point, oval(91, 34, 6, 6)[:-1], EDGE)
    s.tube([point(x, z) for x, z in ((91, 34), (100, 41), (108, 47),
                                     (115, 49), (119, 46), (120, 42))], 1.5, EDGE)

    chart_line(s, point, [(16, 29), (27, 29), (27, 45), (48, 45), (48, 29), (61, 29)], DETAIL)
    for x, z in ((16, 29), (37, 45), (61, 29)):
        s.face([point(u, v) for u, v in oval(x, z, 4, 4)[:-1]], EDGE)
    warning(s, *point(73, -8), size=36)
