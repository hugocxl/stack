from geometry import BOLD, DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A strapped pallet load displays a maximum-load placard with a weight symbol."


def draw(s):
    for x in (-35, -3, 29):
        for y in (-23, 17):
            s.box(x, y, 0, 7, 10, 8, 1)
    for y in (-26, -13, 0, 13, 24):
        s.box(-38, y, 8, 76, 8, 4, 1)
    s.box(-33, -23, 12, 66, 47, 50, 1.5)
    s.line([(0, -22, 62), (0, 24, 62), (0, 24, 12)], DETAIL)
    s.line([(-32, 24, 37), (33, 24, 37), (33, -22, 37)], DETAIL)
    for x in (-24, 23):
        for u in (x, x + 4):
            s.line([(u, -22, 62), (u, 24, 62), (u, 24, 12)], DETAIL)
    s.box(-19, 24, 22, 39, 3, 31, 2)
    bezel(s, -16, 27, 25, 33, 25, DETAIL, 1)
    s.line([(a, 27, b) for a, b in oval(1, 42, 4, 4, count=24)], EDGE)
    s.face([(a, 27, b) for a, b in [(-5, 39), (7, 39), (12, 28), (-10, 28)]], EDGE)
    s.line([(-11, 27, 47), (13, 27, 47)], BOLD)
