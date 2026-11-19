from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, lens_outline, question_mark, rule, speech_bubble, upright_face

DESCRIPTION = "A phone search screen pairs a spoken-style question bubble with an attached answer row."


def draw(s):
    def p(x, z):
        return .68*x, -.32*x - .10*z, z

    upright_face(s, p, rounded(0, 0, 76, 110, 9), 8)
    closed_outline(s, p, rounded(6, 9, 64, 91, 5), DETAIL)
    rule(s, p, 29, 105, 18, DETAIL)
    search = rounded(11, 21, 54, 71, 3)
    closed_outline(s, p, search, EDGE)
    rule(s, p, 11, 46, 54, EDGE)
    lens_outline(s, p, 21, 81, 4.4)
    rule(s, p, 32, 80, 25)

    def speech(x, z):
        return p(22 + x, 54 + z)

    speech_bubble(s, speech, 32, 19, tail=.25, depth=0)
    question_mark(s, speech, 16, 9, 8.1)
    rule(s, p, 18, 37, 36, EDGE)
    rule(s, p, 18, 29, 27, DETAIL)
