from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import rule, sparkle, upright_face

DESCRIPTION = "An editor shows a sparkle-marked inline completion at the end of a partially written line."


def draw(s):
    def p(x, z):
        return .29*x, -.71*x - .24*z, z

    upright_face(s, p, rounded(0, 0, 112, 67, 7), 9)
    for z, width in ((54, 72), (45, 49), (20, 78), (11, 56)):
        rule(s, p, 10, z, width, DETAIL)
    rule(s, p, 10, 33, 31, EDGE)
    s.line([p(46, 26), p(46, 40)], DETAIL)
    completion = rounded(51, 24, 55, 18, 4)
    s.face([p(x, z) for x, z in completion], EDGE)
    sparkle(s, p, 61, 33, 6.5)
    rule(s, p, 71, 33, 24, EDGE)
