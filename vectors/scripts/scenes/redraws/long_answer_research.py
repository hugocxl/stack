from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, magnifier, rule, upright_face

DESCRIPTION = "A magnifier rests over a bound research report with section headings and short footnotes."


def draw(s):
    def point(x, z):
        return .61*x, -.39*x - .33*z, .93*z

    upright_face(s, point, rounded(0, 0, 93, 112, 5), 11)
    chart_line(s, point, [(9, 2), (9, 110)], EDGE)
    chart_line(s, point, [(14, 5), (88, 5), (88, 107), (14, 107)], DETAIL)
    rule(s, point, 20, 95, 44, EDGE)
    for z, widths in ((78, (24, 54, 51, 37)), (46, (29, 57, 42))):
        for index, width in enumerate(widths):
            rule(s, point, 20, z - 7*index, width, EDGE if index == 0 else DETAIL)
    rule(s, point, 20, 19, 51, EDGE)
    for x, width in ((20, 20), (46, 16)):
        rule(s, point, x, 11, width)
    x, y, z = point(70, 51)
    magnifier(s, x, y + 2, z, 16, direction=(.89, -.46))
