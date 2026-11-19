from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import chart_line, currency, rule

DESCRIPTION = "A renewal ledger shows a solid revenue history extending into a dashed forecast."


def draw(s):
    s.box(0, -23, 0, 107, 23, 93, 4)
    s.box(0, -26, 0, 11, 28, 93, 3)
    p = lambda x, z: (x, 0, z)
    rule(s, p, 26, 77, 37, DETAIL)
    glyph(s, "refresh", 86, 0, 77, 12, EDGE)
    currency(s, p, 24, 56, .8, EDGE)
    s.line([p(21, 44), p(21, 15), p(97, 15)], DETAIL)
    chart_line(s, p, [(22, 22), (32, 28), (43, 26), (53, 36), (64, 39)], BOLD)
    chart_line(s, p, [(64, 39), (76, 47), (86, 50), (97, 60)], EDGE, dash=(4.5, 3.2))
