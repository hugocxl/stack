from geometry import BOLD, DETAIL
from scenes.redraws._w2 import chart_line

DESCRIPTION = "A stocked shop shelf carries a demand chart that rises into a dashed forecast."


def draw(s):
    s.box(0, -30, 0, 7, 40, 66, 2)
    s.box(103, -30, 0, 7, 40, 66, 2)
    s.box(0, -28, 9, 110, 39, 5, 2)
    s.box(0, -28, 40, 110, 39, 5, 2)
    s.box(16, -14, 45, 35, 20, 19, 2)
    s.line([(24, 6, 57), (43, 6, 57)], DETAIL)
    s.line([(24, 6, 51), (35, 6, 51)], DETAIL)
    s.disk(75, -5, 14, 12, 12, 24)
    s.ellipse(75, -5, 38, 8, 8, DETAIL)
    s.ellipse(75, -5, 22, 12, 12, DETAIL, start=-42, end=131)
    s.box(0, -17, 66, 110, 10, 79, 3)

    def p(x, z):
        return x, -7, z

    s.line([p(12, 130), p(12, 74), p(99, 74)], DETAIL)
    chart_line(s, p, [(15, 78), (29, 84), (41, 88), (53, 102), (65, 111)], BOLD)
    chart_line(s, p, [(65, 111), (79, 125), (97, 138)], BOLD, dash=(5, 3))
