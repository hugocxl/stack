from math import sin, pi

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, rule

DESCRIPTION = "A chart recorder aligns an original signal, a rising trend, and a repeating seasonal wave on three strips."


def draw(s):
    s.box(0, -28, 0, 120, 28, 96, 5)
    s.disk(14, 1, 7, 4, 4, 81, DETAIL)
    s.disk(14, 1, 86, 6, 6, 5, EDGE)

    def p(x, z):
        return x, 3 + max(x - 117, 0)*.38, z

    paper = [(14, 7), (117, 7), (132, 7), (129, 14), (132, 21),
             (132, 73), (129, 80), (132, 87), (117, 87), (14, 87)]
    s.face([p(x, z) for x, z in paper], EDGE)
    for z in (32, 62):
        rule(s, p, 18, z, 108, DETAIL)
    for x in (33, 61, 89, 117):
        chart_line(s, p, [(x, 11), (x, 84)], DETAIL, dash=(2, 4))
    xs = range(21, 122)
    wave = lambda x: sin((x - 21)*2*pi/28)
    chart_line(s, p, [(x, 69 + (x - 21)*.10 + 6.3*wave(x)) for x in xs], BOLD)
    chart_line(s, p, [(x, 41 + (x - 21)*.13) for x in xs], EDGE)
    chart_line(s, p, [(x, 16 + 7*wave(x)) for x in xs], EDGE)
