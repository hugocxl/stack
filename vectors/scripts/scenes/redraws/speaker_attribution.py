from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, folded_sheet, rule, upright_face

DESCRIPTION = "A transcript has a microphone tag attached to the first utterance and a second block of dialogue below."


def draw(s):
    def p(x, z):
        return .61*x, -.39*x - .23*z, z

    folded_sheet(s, p, 87, 105, fold=14, depth=7)
    rule(s, p, 14, 90, 40, EDGE)
    for z, length in ((54, 56), (46, 44), (26, 54), (18, 57), (10, 37)):
        rule(s, p, 17, z, length, DETAIL)
    rule(s, p, 17, 36, 20, EDGE)

    def tag(x, z):
        return p(x - 17, z + 61)

    upright_face(s, tag, rounded(0, 0, 58, 24, 4), 4)
    closed_outline(s, tag, rounded(11, 9, 7, 12, 3.5), EDGE)
    chart_line(s, tag, [(8, 13), (8, 11), (10, 7), (14.5, 5.5), (19, 7),
                        (21, 11), (21, 13)], EDGE)
    chart_line(s, tag, [(14.5, 5.5), (14.5, 3)], EDGE)
    rule(s, tag, 28, 12, 22, BOLD)
