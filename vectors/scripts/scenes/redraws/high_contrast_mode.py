from math import sqrt

from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import BACK, plate, screen

DESCRIPTION = "A thick circular dial faces the viewer, its left half hatched dark and its right half open."


def draw(s):
    at = screen()
    plate(s, at, oval(0, 0, 44, 44, count=96)[:-1], 9, BACK)
    r = 34
    s.line([at(u, v) for u, v in oval(0, 0, r, r, count=96)], EDGE)
    s.line([at(0, r), at(0, -r)], EDGE)
    # Hatch the dark half with 45-degree lines u = v + c, clipped to the left half-disc.
    for k in range(-9, 4):
        c = k*6.2
        disc = 2*r*r - c*c
        if disc <= 0:
            continue
        lo = (-c - sqrt(disc))/2
        hi = min((-c + sqrt(disc))/2, -c)
        if hi - lo > 1.5:
            s.line([at(lo + c, lo), at(hi + c, hi)], DETAIL)
