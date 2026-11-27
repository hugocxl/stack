from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import BACK, person, plate, screen

DESCRIPTION = "A thick progress ring, three quarters complete, surrounds three member figures."


def ring_arc(a0, a1, r, w):
    outer = [((r + w/2)*cos(radians(a)), (r + w/2)*sin(radians(a))) for a in range(a0, a1 + 1, 4)]
    inner = [((r - w/2)*cos(radians(a)), (r - w/2)*sin(radians(a))) for a in range(a1, a0 - 1, -4)]
    return outer + inner


def draw(s):
    at = screen()
    s.line([at(46*cos(radians(a)), 46*sin(radians(a))) for a in range(0, 361, 4)], DETAIL)
    plate(s, at, ring_arc(-180, 90, 46, 12), 6, BACK)
    for u, v, k in ((-14, -4, 22), (14, -4, 22), (0, 2, 26)):
        person(s, at, u, v, k)
