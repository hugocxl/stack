from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_marker, printed_glyph, rule, standing_notebook

DESCRIPTION = "Three distinct clock faces sit beside three topic lines on a spiral meeting agenda."


def draw(s):
    point = standing_notebook(s, 100, 98)
    rule(s, point, 13, 75, 44, EDGE)
    for z, angle, length in ((55, 0, 42), (34, -45, 48), (13, -96, 37)):
        chart_marker(s, point, 21, z, 7.8, EDGE)
        turn = radians(angle)

        def dial(x, v):
            return point(21 + x*cos(turn) - v*sin(turn), z + x*sin(turn) + v*cos(turn))

        printed_glyph(s, dial, "clock", 0, 0, 6, EDGE)
        rule(s, point, 36, z + 3, length, EDGE)
        rule(s, point, 36, z - 3.5, length*.57, DETAIL)
