from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import board, chart_line, closed_outline

DESCRIPTION = "A monitoring chart shows a level threshold above its trend and a shield on the upper corner of its frame."


def draw(s):
    p = board(s, 124, 74, run=.17, depth=12, level=True)
    s.line([p(12, 54), p(12, 12), p(111, 12)], DETAIL)
    chart_line(s, p, [(12, 51), (94, 51)], BOLD)
    chart_line(s, p, [(15, 26), (27, 33), (43, 28), (55, 41),
                     (69, 35), (85, 43), (106, 37)], EDGE)
    closed_outline(s, p, [(96, 63), (106, 67), (116, 63), (115, 53),
                          (111, 48), (106, 45), (101, 48), (97, 53)], EDGE)
