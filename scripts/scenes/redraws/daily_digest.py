from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import calendar_header, panel, rect

DESCRIPTION = "A folded newsletter carries a calendar masthead and short story summaries beside a lead picture."


def draw(s):
    def face(x, z):
        return x, -.54*z, z

    outline = rounded(0, 0, 73, 62, 3)
    panel(s, outline, face, 6.2)
    calendar_header(s, face, 9, 43, 1)
    s.line([face(32, 51), face(63, 51)], EDGE)
    s.line([face(32, 45), face(54, 45)])
    s.line([face(0, 38), face(73, 38)], EDGE)
    rect(s, face, 9, 9, 22, 23, 1.5, EDGE)
    s.line([face(9, 13), face(17, 23), face(23, 16), face(28, 20), face(31, 16)])
    for z, end in ((29, 64), (24, 57), (17, 62), (12, 53)):
        s.line([face(37, z), face(end, z)], EDGE if z in (29, 17) else DETAIL)
