from math import sqrt

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._sf import BACK, capsule, plate, screen

DESCRIPTION = "A contrast dial with a hatched half sits above a slider whose knob sets the level."


def draw(s):
    at = screen()
    d = lambda u, v: at(u, v + 22)
    plate(s, d, oval(0, 0, 36, 36, count=96)[:-1], 7, BACK)
    r = 28
    s.line([d(0, r), d(0, -r)], EDGE)
    s.line([d(u, v) for u, v in oval(0, 0, r, r, count=96)], EDGE)
    for k in range(-7, 3):
        c = k*6
        disc = 2*r*r - c*c
        if disc > 0:
            lo, hi = (-c - sqrt(disc))/2, min((-c + sqrt(disc))/2, -c)
            if hi - lo > 1.5:
                s.line([d(lo + c, lo), d(hi + c, hi)], DETAIL)
    t = lambda u, v: at(u - 48, v - 40)
    plate(s, t, capsule(96, 12), 4, BACK)
    s.line([t(8, 6), t(60, 6)], BOLD)
    plate(s, lambda u, v: t(60 + u, 6 + v), oval(0, 0, 10, 10, count=40)[:-1], 4, BACK)
