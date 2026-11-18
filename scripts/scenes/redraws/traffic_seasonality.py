from math import cos, pi

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w2 import chart_line, chart_marker

DESCRIPTION = "A ring-bound desk calendar shows three regularly spaced web-traffic peaks."


def draw(s):
    def p(x, z):
        return x, -.35 * z, z

    s.face([(0, -48, 0), (108, -48, 0), (108, -30, 83), (0, -30, 83)], EDGE)
    s.face([p(0, 0), p(108, 0), p(108, 83), p(0, 83)], EDGE)
    for x in (19, 89):
        s.tube([p(x, 77), (x, -24, 88), (x, -32, 92), (x, -38, 84)], 2.1, EDGE)
    s.line([p(0, 65), p(108, 65)], EDGE)
    chart_marker(s, p, 54, 74, 6.2, EDGE)
    chart_line(s, p, oval(54, 74, 2.7, 6, count=20), DETAIL)
    s.line([p(48, 74), p(60, 74)], DETAIL)
    s.line([p(10, 59), p(10, 15), p(99, 15)], DETAIL)
    for x in (23, 54, 85):
        chart_line(s, p, [(x, 19), (x, 54)], DETAIL, dash=(2, 3))
        s.line([p(x, 15), p(x, 9)], EDGE)
    chart_line(s, p, [(x, 22 + 33*(.5 + .5*cos((x - 23)*2*pi/31))**1.6)
                     for x in range(11, 99)], BOLD)
