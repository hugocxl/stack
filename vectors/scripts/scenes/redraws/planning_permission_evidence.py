from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, face_magnifier, folded_sheet

DESCRIPTION = "A magnifier frames the proposed building outline on a site plan with a clearly marked parcel boundary."


def draw(s):
    def point(x, z):
        return .74*x, -.26*x - .76*z, .55*z

    folded_sheet(s, point, 97, 78, fold=9, depth=5)
    closed_outline(s, point, [(10, 14), (69, 10), (83, 28), (75, 64), (17, 67)], EDGE)
    closed_outline(s, point, [(29, 26), (50, 26), (50, 34), (60, 34),
                              (60, 53), (29, 53)], EDGE)
    chart_line(s, point, [(18, 9), (69, 5), (89, 27)], DETAIL)
    chart_line(s, point, [(33, 26), (32, 14)], DETAIL)
    chart_line(s, point, [(40, 26), (39, 14)], DETAIL)

    def glass(x, z):
        a, b, c = point(x, z)
        return a, b + 2, c + 5

    face_magnifier(s, glass, 45, 39, 24, direction=(.76, -.65))
