from geometry import DETAIL, EDGE
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A capped archive tube stands beside a rolled drawing whose sheet unrolls to show a floor plan."


def draw(s):
    turned(s, [(13, 0), (13, 66)], -54, 0, 0, steps=1)
    turned(s, [(14.5, 62), (14.5, 76), (11, 78)], -54, 0, 0, steps=2)
    s.face([(-10, -30, 0), (60, -30, 0), (60, 30, 0), (-10, 30, 0)], EDGE)
    s.tube([(-10, -30, 5), (-10, 30, 5)], 5, EDGE)
    plan = [(6, -18), (44, -18), (44, 20), (6, 20), (6, -18)]
    s.line([(x, y, 0) for x, y in plan], EDGE)
    s.line([(26, -18, 0), (26, 4, 0)], DETAIL)
    s.line([(26, 10, 0), (26, 20, 0)], DETAIL)
    s.line([(6, 2, 0), (20, 2, 0)], DETAIL)
