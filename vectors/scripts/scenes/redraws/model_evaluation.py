from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import BACK, arc, plate, screen

DESCRIPTION = "A semicircular score gauge points past its marked pass threshold, with a check badge."


def draw(s):
    at = screen()
    R = 52
    plate(s, at, arc(0, 0, R, 0, 180, 48) + [(-R, -6), (R, -6)], 8, BACK)
    s.line([at(u, v) for u, v in arc(0, 0, R - 9, 8, 172, 40)], DETAIL)
    for a in range(10, 171, 20):
        r0, r1 = R - 9, R - 15
        s.line([at(r0*cos(radians(a)), r0*sin(radians(a))), at(r1*cos(radians(a)), r1*sin(radians(a)))], DETAIL)
    t = 60
    s.line([at((R - 4)*cos(radians(t)), (R - 4)*sin(radians(t))), at((R - 22)*cos(radians(t)), (R - 22)*sin(radians(t)))], EDGE)
    n = 38
    s.line([at(0, 0), at(36*cos(radians(n)), 36*sin(radians(n)))], BOLD)
    s.line([at(4*cos(radians(a)), 4*sin(radians(a))) for a in range(0, 361, 20)], BOLD)
    badge(s, "check", *_screen(0, 0, 0, 52, 2), 13)
