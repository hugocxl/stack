from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, printed_glyph, rule, upright_face

DESCRIPTION = "A clipped construction site plan sits above a short safety checklist on a clipboard."


def draw(s):
    def p(x, z):
        return .79*x, -.21*x - .63*z, .7*z

    upright_face(s, p, rounded(0, 0, 94, 96, 4), 7)
    closed_outline(s, p, [(8, 9), (86, 9), (86, 88), (8, 88)], DETAIL)
    upright_face(s, p, [(28, 83), (66, 83), (66, 91), (59, 91),
                        (54, 98), (40, 98), (35, 91), (28, 91)], 3)
    chart_line(s, p, [(19, 53), (19, 76), (73, 76), (73, 60), (49, 60),
                      (49, 53), (19, 53)], EDGE)
    chart_line(s, p, [(38, 76), (38, 63), (49, 63), (49, 60)], DETAIL)
    for z, length in ((36, 41), (22, 34)):
        printed_glyph(s, p, "check", 24, z, 6, EDGE)
        rule(s, p, 37, z, length)
