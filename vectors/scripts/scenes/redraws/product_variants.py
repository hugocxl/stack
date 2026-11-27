from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import shirt

DESCRIPTION = "Three matching T-shirts stand in a row, plain, striped and dotted."


def draw(s):
    for i in range(3):
        at = shirt(s, -96 + i*58, -i*6, 0, .8)
        if i == 1:
            for v in (14, 22, 30, 38):
                s.line([at(14, v), at(46, v)], DETAIL)
        if i == 2:
            for u, v in ((22, 16), (38, 16), (30, 26), (22, 36), (38, 36)):
                s.line([at(u + a, v + b) for a, b in oval(0, 0, 2.4, 2.4, count=16)], EDGE)
