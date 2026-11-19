from math import pi, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, currency, rule, upright_face

DESCRIPTION = "An insulation estimate shows a stud-wall cross-section with looping batts beside the quoted amount."


def draw(s):
    def p(x, z):
        return .68*x, -.32*x - .36*z, .9*z

    upright_face(s, p, [(0, 0), (121, 0), (121, 69), (0, 69)], 5)
    closed_outline(s, p, [(10, 15), (68, 15), (68, 55), (10, 55)], EDGE)
    for x in (16, 39, 62):
        chart_line(s, p, [(x, 15), (x, 55)], EDGE)
    for x in (27, 50):
        loops = [(x + 7*sin(i*pi/6), 18 + 35*i/24) for i in range(25)]
        chart_line(s, p, loops, EDGE)
    rule(s, p, 80, 49, 29, EDGE)
    rule(s, p, 80, 40, 23)
    currency(s, p, 88, 22, .92, BOLD)
    rule(s, p, 98, 22, 12, EDGE)
