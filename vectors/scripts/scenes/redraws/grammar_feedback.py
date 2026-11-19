from math import pi, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, desk_sheet, rule

DESCRIPTION = "A proofreading wave underlines one short phrase in a folded writing page."


def draw(s):
    point = desk_sheet(s, 82, 101)
    for z, start, width in ((82, 12, 44), (69, 12, 57), (56, 12, 16),
                            (56, 35, 28), (37, 12, 55), (24, 12, 39)):
        rule(s, point, start, z, width, EDGE if start == 35 else DETAIL)
    chart_line(s, point, [(34 + i, 47 + 2*sin(i*pi/4)) for i in range(30)], BOLD)
