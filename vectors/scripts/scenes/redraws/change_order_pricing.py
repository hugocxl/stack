from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, currency, desk_sheet, printed_glyph, rule

DESCRIPTION = "A change order crosses out an original amount and highlights its revised price with a plus and a currency mark."


def draw(s):
    p = desk_sheet(s, 105, 87)
    chart_line(s, p, [(14, 66), (14, 78), (35, 78), (35, 66), (25, 66),
                      (25, 72), (19, 72), (19, 66), (14, 66)], EDGE)
    rule(s, p, 46, 74, 30, EDGE)
    rule(s, p, 15, 50, 30)
    rule(s, p, 65, 50, 20, DETAIL)
    chart_line(s, p, [(62, 47), (88, 54)], EDGE)
    closed_outline(s, p, [(12, 16), (94, 16), (94, 38), (12, 38)], EDGE)
    rule(s, p, 19, 27, 25, EDGE)
    printed_glyph(s, p, "plus", 64, 27, 6, EDGE)
    currency(s, p, 81, 27, .98, BOLD)
