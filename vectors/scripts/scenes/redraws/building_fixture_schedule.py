from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, upright_face

DESCRIPTION = "A faucet heads a two-column fixture table on a thick tabbed specification binder."


def draw(s):
    def p(x, z):
        return .73*x, -.27*x - .32*z, .94*z

    # The spine and projecting divider index signal a durable specification binder.
    upright_face(s, p, [(0, 0), (112, 0), (112, 81), (0, 81)], 10)
    upright_face(s, p, [(102, 47), (117, 47), (117, 62), (102, 62)], 4)
    upright_face(s, p, list(rounded(0, 0, 108, 84, 3)), 3)
    chart_line(s, p, [(10, 2), (10, 82)], EDGE)
    chart_line(s, p, [(21, 56), (21, 63), (23, 69), (29, 74), (37, 74),
                      (43, 70), (44, 64), (38, 64), (37, 68), (29, 68), (28, 56)], EDGE)
    chart_line(s, p, [(16, 56), (33, 56)], EDGE)
    chart_line(s, p, [(54, 69), (86, 69)], DETAIL)
    chart_line(s, p, [(54, 61), (74, 61)], DETAIL)
    closed_outline(s, p, [(19, 15), (94, 15), (94, 47), (19, 47)], EDGE)
    chart_line(s, p, [(64, 47), (64, 15)], DETAIL)
    for z in (26, 37):
        chart_line(s, p, [(19, z), (94, z)], DETAIL)
    for z in (20, 31, 42):
        chart_line(s, p, [(25, z), (49, z)], DETAIL)
        chart_line(s, p, [(70, z), (85, z)], DETAIL)
