from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, closed_outline, rule, upright_face

DESCRIPTION = "An invitation card with an overhead meeting-table pictogram carries an X badge on its upper corner."


def draw(s):
    def point(x, z):
        return .86*x, -.14*x - .22*z, .9*z

    upright_face(s, point, rounded(0, 0, 105, 76, 6), 6)
    closed_outline(s, point, oval(48, 47, 23, 9), EDGE)
    for x, z in ((30, 61), (49, 64), (68, 61), (37, 32), (59, 32)):
        closed_outline(s, point, rounded(x - 4, z - 2.5, 8, 5, 2), EDGE)
    rule(s, point, 18, 18, 55, DETAIL)
    chart_line(s, point, [(18, 10), (54, 10)], DETAIL)
    badge(s, "x", *point(104, 75), 13)
