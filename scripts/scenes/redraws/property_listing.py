from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, currency, rule, upright_face

DESCRIPTION = "A real-estate listing card features a large house thumbnail above its price and two details."


def draw(s):
    def p(x, z):
        return .27*x - .31*z, -.73*x, .91*z

    upright_face(s, p, rounded(0, 0, 100, 91, 5), 5)
    closed_outline(s, p, [(9, 37), (91, 37), (91, 82), (9, 82)], DETAIL)
    chart_line(s, p, [(26, 44), (26, 59), (47, 74), (69, 59), (69, 44),
                      (26, 44)], EDGE)
    chart_line(s, p, [(21, 56), (47, 76), (75, 56)], EDGE)
    chart_line(s, p, [(34, 58), (41, 58), (41, 51), (34, 51), (34, 58)], DETAIL)
    chart_line(s, p, [(51, 44), (51, 57), (60, 57), (60, 44)], DETAIL)
    currency(s, p, 18, 21, .92, BOLD)
    rule(s, p, 30, 21, 22, EDGE)
    rule(s, p, 66, 25, 19)
    rule(s, p, 66, 17, 14)
