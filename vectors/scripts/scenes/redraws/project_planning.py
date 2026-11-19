from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, printed_glyph, rule, upright_face

DESCRIPTION = "A framed project board holds task cards in three workflow columns marked with a dot, play symbol, and check."


def planning_board(s, *, lanes):
    width = 44*lanes + 12
    height = 100

    def point(x, z):
        return .76*x, -.24*x - .28*z, .92*z

    upright_face(s, point, rounded(0, 0, width, height, 4), 9)
    closed_outline(s, point, rounded(5, 5, width - 10, height - 10, 2), EDGE)
    rule(s, point, 5, 76, width - 10, EDGE)
    for lane in range(1, lanes):
        x = 6 + 44*lane
        s.line([point(x, 5), point(x, 95)], EDGE)
    return point


def lane_card(s, point, lane, z):
    x = 11 + 44*lane

    def face(u, v):
        a, b, c = point(u, v)
        return a, b + 2, c

    upright_face(s, face, rounded(x, z, 34, 16, 2), 2)
    rule(s, face, x + 6, z + 10, 20, EDGE)
    rule(s, face, x + 6, z + 5, 13, DETAIL)


def draw(s):
    point = planning_board(s, lanes=3)
    headings = (("dot", (54, 33)), ("play", (54,)), ("check", (54, 33, 12)))
    for lane, (kind, rows) in enumerate(headings):
        printed_glyph(s, point, kind, 16 + 44*lane, 86, 7, EDGE)
        rule(s, point, 24 + 44*lane, 86, 16, DETAIL)
        for z in rows:
            lane_card(s, point, lane, z)
