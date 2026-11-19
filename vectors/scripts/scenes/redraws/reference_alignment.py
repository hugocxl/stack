from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, chart_marker, closed_outline, upright_face

DESCRIPTION = "A lightbox registers a solid sailboat drawing against a nearly superimposed dashed reference and three alignment targets."


def draw(s):
    def point(x, z):
        return .55*x, -.45*x - .53*z, .70*z

    upright_face(s, point, rounded(0, 0, 106, 86, 8), 12)
    closed_outline(s, point, rounded(8, 8, 90, 70, 4), DETAIL)
    sail = [(37, 32), (60, 32), (60, 65), (37, 32)]
    hull = [(29, 25), (77, 25), (68, 15), (41, 15), (29, 25)]
    chart_line(s, point, [(x + 4, z + 4) for x, z in sail], DETAIL, dash=(3, 2.5))
    chart_line(s, point, [(x + 4, z + 4) for x, z in hull], DETAIL, dash=(3, 2.5))
    chart_line(s, point, sail, BOLD)
    chart_line(s, point, hull, EDGE)
    for x, z in ((19, 65), (86, 65), (19, 21)):
        chart_marker(s, point, x, z, 3.5, EDGE)
        chart_line(s, point, [(x - 6, z), (x + 6, z)], DETAIL)
        chart_line(s, point, [(x, z - 6), (x, z + 6)], DETAIL)
