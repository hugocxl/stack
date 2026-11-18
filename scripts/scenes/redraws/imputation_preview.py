from geometry import BOLD, DETAIL
from scenes.redraws._w2 import chart_line, grid_table

DESCRIPTION = "A dashed data-table cell contains one faint preview entry among the existing values."


def draw(s):
    p = grid_table(s, preview=True)
    chart_line(s, p, [(37, 20), (62, 20), (62, 34), (37, 34), (37, 20)],
               BOLD, dash=(4.4, 2.6))
    s.line([p(44, 27), p(55, 27)], DETAIL)
