from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, printed_glyph, rule, upright_face

DESCRIPTION = "A tent calendar headed by a house aligns three covered warranty milestones with three date cells."


def draw(s):
    def p(x, z):
        return .79*x, -.21*x - .47*z, .9*z

    s.face([(0, -56, 0), (80, -71, 0), p(101, 83), p(0, 83)], EDGE)
    upright_face(s, p, [(0, 0), (101, 0), (101, 83), (0, 83)], 3)
    for x in (16, 85):
        a, b, c = p(x, 78)
        s.tube([(a, b + .5, c), (a, b - 1, c + 9), (a, b - 8, c + 9),
                (a, b - 11, c + 2)], 1.25)
    chart_line(s, p, [(41, 51), (41, 65), (50, 74), (60, 65),
                      (60, 51), (41, 51)], EDGE)
    chart_line(s, p, [(48, 51), (48, 59), (53, 59), (53, 51)], DETAIL)
    rule(s, p, 8, 45, 85, EDGE)
    for x in (22, 50, 79):
        closed_outline(s, p, [(x - 9, 23), (x + 9, 23), (x + 9, 38), (x - 9, 38)], EDGE)
        rule(s, p, x - 5, 34, 10)
        printed_glyph(s, p, "check", x, 12, 6, EDGE)
