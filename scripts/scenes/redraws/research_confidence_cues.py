from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, rule, upright_face

DESCRIPTION = "A source index card carries a five-segment confidence scale with a marker above its fourth cell."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x - .31*z, z

    upright_face(s, point, rounded(0, 0, 112, 70, 4), 8)
    rule(s, point, 13, 53, 56, EDGE)
    rule(s, point, 13, 42, 38, DETAIL)
    closed_outline(s, point, rounded(13, 15, 85, 14, 2), EDGE)
    for x in (30, 47, 64, 81):
        chart_line(s, point, [(x, 15), (x, 29)], DETAIL)
    s.face([point(x, z) for x, z in [(67, 34), (78, 34), (72.5, 29)]], BOLD)
