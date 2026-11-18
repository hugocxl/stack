from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, upright_face

DESCRIPTION = "An open cadastral map compares two adjoining lots with matching dimension ticks and visibly different widths."


def draw(s):
    def p(x, z):
        fold = abs(x - 38) * .16
        return .75*x, -.25*x - .45*z + fold, .88*z

    # A folded map stands on its lower edge, with each lot printed on a panel.
    for left, right in ((0, 38), (38, 126)):
        points = [(left, 0), (right, 0), (right, 67), (left, 67)]
        upright_face(s, p, points, 3)
    for x0, x1 in ((12, 38), (38, 112)):
        closed_outline(s, p, [(x0, 21), (x1, 21), (x1, 56), (x0, 56)], EDGE)
        chart_line(s, p, [(x0, 12), (x1, 12)], DETAIL)
    for x in (12, 38, 112):
        chart_line(s, p, [(x, 8), (x, 17)], EDGE)
    chart_line(s, p, [(4, 55), (8, 62), (38, 62), (87, 62), (121, 58)], DETAIL)
    chart_line(s, p, [(21, 29), (30, 29), (30, 40), (21, 40), (21, 29)], DETAIL)
    chart_line(s, p, [(55, 28), (71, 28), (71, 38), (63, 38), (63, 47),
                      (55, 47), (55, 28)], DETAIL)
