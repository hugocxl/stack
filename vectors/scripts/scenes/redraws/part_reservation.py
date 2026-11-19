from math import cos, pi, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A spare gear has a recessed center bore and a clock badge against one of its teeth."


def draw(s):
    outer = []
    for tooth in range(10):
        for offset, radius in ((-.50, 31), (-.30, 31), (-.24, 40),
                               (.24, 40), (.30, 31)):
            angle = 2*pi*(tooth + offset)/10
            outer.append((radius*cos(angle), radius*sin(angle)))
    for i, (x, y) in enumerate(outer):
        u, v = outer[(i + 1) % len(outer)]
        if (v - y) > (u - x):
            s.face([(x, y, 0), (u, v, 0), (u, v, 10), (x, y, 10)], EDGE)
    s.ellipse(0, 0, 3, 11, 11, DETAIL, start=188, end=350)
    s.face([(*p, 10) for p in outer],
           openings=[[(*p, 10) for p in oval(0, 0, 11, 11)[:-1]]])
    s.ellipse(0, 0, 10, 17, 17, DETAIL)
    badge(s, "clock", 25, -24, 18, 13)
