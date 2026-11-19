from geometry import DETAIL, EDGE
from scenes.redraws._w2 import plan_magnifier

DESCRIPTION = "A magnifier frames the raised decision block where a workflow branches into two steps."


def draw(s):
    s.line([(17, 34, 4), (74, 34, 4)], EDGE)
    s.line([(94, 9, 4), (74, 9, 4), (74, 64, 4), (94, 64, 4)], EDGE)
    for x, y in ((0, 24), (90, -1), (90, 54)):
        s.box(x, y, 0, 22, 20, 8, 2)
        s.line([(x + 6, y + 10, 8), (x + 16, y + 10, 8)], DETAIL)
    diamond = [(35, 34), (50, 19), (65, 34), (50, 49)]
    s.solid(diamond, 0, 10)
    plan_magnifier(s, 52, 36, 13, 19, direction=(0, 1))
