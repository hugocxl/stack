from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, rule, upright_face

DESCRIPTION = "A hardcover writing guide carries a single speech bubble on its front cover."


def draw(s):
    def point(x, z):
        return .81*x, -.19*x - .17*z, z

    upright_face(s, point, rounded(0, 0, 75, 94, 5), 17)
    chart_line(s, point, [(10, 4), (10, 90)], EDGE)
    for offset in (5, 9):
        a, b = point(75, 8), point(75, 87)
        s.line([(x - offset*.25, y - offset*.75, z) for x, y, z in (a, b)], DETAIL)
    bubble = [(24, 41), (24, 68), (62, 68), (62, 41),
              (41, 41), (30, 32), (31, 41)]
    closed_outline(s, point, bubble, EDGE)
    rule(s, point, 31, 58, 23)
    rule(s, point, 31, 50, 16)
