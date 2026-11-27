from math import cos, radians, sin

from geometry import EDGE

DESCRIPTION = "A thick energy-mix disc splits into a sun sector and a wind sector."


def sector(s, a0, a1, r, h, dx, dy):
    ring = [(dx, dy)] + [(dx + r*cos(radians(a)), dy + r*sin(radians(a))) for a in range(a0, a1 + 1, 4)]
    s.solid(ring, 0, h)


def draw(s):
    sector(s, 160, 360, 54, 10, -3, -3)
    sector(s, 0, 160, 54, 10, 4, 4)
    cx, cy = -10, -32
    s.ellipse(cx, cy, 10, 7, 7, EDGE)
    for a in range(0, 360, 45):
        c, q = cos(radians(a)), sin(radians(a))
        s.line([(cx + 10*c, cy + 10*q, 10), (cx + 14*c, cy + 14*q, 10)], EDGE)
    for off in (-9, 0, 9):
        s.line([(14 + off + 3*sin(t/2.5), 30 + t - off, 10) for t in range(-12, 13)], EDGE)
