from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, clipboard, closed_outline, rule

DESCRIPTION = "A clipboard holds a checklist with a bold bracket grouping the first three tasks."


def draw(s):
    top = clipboard(s)

    def point(x, row):
        return x, 96 - row, top

    for row, length in ((62, 37), (49, 31), (36, 40), (17, 29)):
        closed_outline(s, point, [(19, row - 3), (25, row - 3),
                                  (25, row + 3), (19, row + 3)], EDGE)
        rule(s, point, 32, row, length, EDGE if row > 17 else DETAIL)
    chart_line(s, point, [(72, 68), (79, 68), (79, 30), (72, 30)], BOLD)
