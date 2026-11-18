from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_marker, closed_outline, rule, upright_face

DESCRIPTION = "A content recommendation card has a landscape thumbnail, title rules, and an attached star badge."


def draw(s):
    def p(x, z):
        return .87*x, -.13*x - .16*z, z

    upright_face(s, p, rounded(0, 0, 118, 67, 5), 9)
    closed_outline(s, p, rounded(10, 13, 44, 39, 3), EDGE)
    s.line([p(11, 21), p(25, 40), p(36, 28), p(42, 34), p(53, 23)], EDGE)
    chart_marker(s, p, 43, 42, 4, DETAIL)
    for z, length in ((42, 34), (33, 43), (24, 27)):
        rule(s, p, 64, z, length, EDGE if z == 42 else DETAIL)
    badge(s, "star", *p(111, 61), 15)
