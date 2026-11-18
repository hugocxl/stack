from math import exp

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import axes, chart_line, outline

DESCRIPTION = "An oscilloscope compares a narrow high peak with a broad low peak on the same scale."


def draw(s):
    s.box(0, -30, 0, 133, 30, 85, 6)
    outline(s, 7, 0, 8, 97, 70, 4, EDGE)
    p = lambda x, z: (x, 0, z)
    axes(s, p, x=17, y=18, width=79, height=50)
    for z, r in ((25, 6), (47, 6), (66, 4)):
        outline(s, 119 - r, 0, z - r, r*2, r*2, r, EDGE)
        s.line([p(119, z + r*.24), p(119 + r*.45, z + r*.7)], DETAIL)
    xs = range(20, 97)
    chart_line(s, p, [(x, 21 + 46*exp(-((x - 50)/10)**2)) for x in xs], BOLD)
    chart_line(s, p, [(x, 21 + 25*exp(-((x - 63)/26)**2)) for x in xs], EDGE)
