from geometry import BOLD, EDGE
from scenes.redraws._w2 import chart_line, currency, desk_sheet, rule

DESCRIPTION = "A folded contractor quote pairs two itemized construction lines with a prominent currency total."


def draw(s):
    p = desk_sheet(s, 94, 96, fold=17)
    chart_line(s, p, [(13, 69), (13, 79), (30, 79), (30, 69),
                      (13, 69), (9, 69)], EDGE)
    chart_line(s, p, [(13, 79), (21, 87), (30, 79)], EDGE)
    rule(s, p, 44, 78, 22, EDGE)
    for z, length in ((53, 32), (40, 24)):
        rule(s, p, 13, z, length, EDGE)
        rule(s, p, 68, z, 12)
    rule(s, p, 12, 28, 69)
    currency(s, p, 51, 15, .95, BOLD)
    rule(s, p, 63, 15, 18, EDGE)
