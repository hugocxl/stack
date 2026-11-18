from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import board, chart_line, closed_outline, rule

DESCRIPTION = "An evidence clipboard has two completed rows and a dashed outline where an attachment belongs."


def draw(s):
    p = board(s, 89, 91, run=.42, rise=.81, depth=9)
    closed_outline(s, p, rounded(8, 7, 73, 76, 2), DETAIL)
    s.face([p(x, z) for x, z in rounded(28, 77, 33, 13, 4)], EDGE)
    rule(s, p, 35, 85, 19)
    for z, length in ((62, 29), (49, 36)):
        closed_outline(s, p, rounded(18, z - 3.8, 8, 7.6, 1), EDGE)
        glyph(s, "check", *p(22, z), 4.5, EDGE)
        rule(s, p, 33, z, length)
    attachment = [(29, 16), (61, 16), (61, 29), (54, 36), (29, 36), (29, 16)]
    chart_line(s, p, attachment, EDGE, dash=(4, 2.5))
    chart_line(s, p, [(54, 36), (54, 29), (61, 29)], DETAIL, dash=(3, 2))
