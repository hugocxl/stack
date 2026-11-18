from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_line, closed_outline, folded_sheet, rule, upright_face

DESCRIPTION = "A short arrow lifts a marked passage from its source page into a separate quotation card."


def draw(s):
    def p(x, z):
        return .77*x, -.23*x - .14*z, z

    folded_sheet(s, p, 91, 99, depth=5)
    for z, length in ((80, 43), (66, 62), (58, 57), (31, 66), (22, 58), (13, 46)):
        rule(s, p, 12, z, length, EDGE if z == 80 else DETAIL)
    closed_outline(s, p, rounded(9, 41, 56, 10, 2), EDGE)
    rule(s, p, 13, 46, 45)
    ox, oy, oz = p(65, 39)

    def quote(x, z):
        return ox + .68*x + 9, oy - .32*x + 4, oz + z

    arrow(s, [p(66, 46), p(74, 48), p(82, 55)], EDGE, head=6)
    upright_face(s, quote, rounded(16, 22, 54, 32, 4), 4)
    for x in (25, 30):
        chart_line(s, quote, [(x + 2, 46), (x, 43), (x, 39), (x + 2.2, 39)], BOLD)
    rule(s, quote, 38, 42, 24, EDGE)
    rule(s, quote, 38, 34, 17, DETAIL)
