from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, chart_marker, rule, upright_face

DESCRIPTION = "A bound answer packet has three source tabs on its edge with a citation rule leading to each one."


def draw(s):
    def point(x, z):
        return .85*x, -.15*x - .22*z, z

    for z in (18, 39, 60):
        upright_face(s, point, rounded(62, z - 7, 29, 14, 3), 3, EDGE)
    upright_face(s, point, rounded(0, 0, 76, 86, 4), 11, EDGE)
    chart_line(s, point, [(7, 4), (7, 81)], DETAIL)
    rule(s, point, 15, 74, 36, EDGE)
    for z, length in ((60, 40), (39, 33), (18, 37)):
        rule(s, point, 15, z, length, EDGE)
        chart_marker(s, point, 63, z, 2.4, EDGE)
        rule(s, point, 67, z, 18, DETAIL)
