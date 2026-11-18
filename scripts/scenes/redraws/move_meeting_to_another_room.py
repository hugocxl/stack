from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_marker, closed_outline, face_arrow, rule, upright_face

DESCRIPTION = "A meeting invitation has a calendar header and a rightward arrow joining two room doors."


def draw(s):
    def point(x, z):
        return .69*x, -.31*x - .46*z, .86*z

    upright_face(s, point, rounded(0, 0, 114, 77, 6), 7)
    closed_outline(s, point, rounded(12, 49, 22, 20, 2), EDGE)
    rule(s, point, 12, 62, 22, EDGE)
    for x in (17, 28):
        s.line([point(x, 66), point(x, 72)], EDGE)
    rule(s, point, 43, 63, 47, EDGE)
    rule(s, point, 43, 54, 31, DETAIL)
    rule(s, point, 11, 44, 92, DETAIL)

    for x, ink in ((16, DETAIL), (77, EDGE)):
        closed_outline(s, point, [(x, 9), (x, 35), (x + 21, 35), (x + 21, 9)], ink)
        closed_outline(s, point, [(x + 4, 9), (x + 4, 31), (x + 17, 31), (x + 17, 9)], ink)
        chart_marker(s, point, x + 13.5, 18, 1.1, ink)
    face_arrow(s, point, [(44, 22), (69, 22)], BOLD, head=7)
