from math import cos, radians, sin

from geometry import EDGE

DESCRIPTION = "A lidded archival box is marked with a snowflake on its front."


def draw(s):
    W, D, H = 76, 52, 40
    s.box(0, 0, 0, W, D, H, 2)
    s.box(-3, -3, H, W + 6, D + 6, 9, 2.5)
    cx, cz = W/2, 20
    for a in (90, 30, 150):
        c, q = 14*cos(radians(a)), 14*sin(radians(a))
        s.line([(cx - c, D, cz - q), (cx + c, D, cz + q)], EDGE)
        for sgn in (1, -1):
            tx, tz = cx + sgn*c*.62, cz + sgn*q*.62
            for b in (a + 45, a - 45):
                s.line([(tx, D, tz), (tx + sgn*4.5*cos(radians(b)), D, tz + sgn*4.5*sin(radians(b)))], EDGE)
