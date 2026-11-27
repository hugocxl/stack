from geometry import EDGE
from scenes.redraws._sf import BACK, bubble, plate, screen, smooth

DESCRIPTION = "A thick speech bubble faces the viewer with a telephone handset standing out from its face."


def draw(s):
    at = screen()
    w, h = 112, 78
    plate(s, lambda u, v: at(u - w/2, v - h/2 + 6), bubble(w, h, 24, (.24, 14, 16)), 9, BACK)
    grip = smooth([(-17, 22), (-23, 10), (-17, -6), (-4, -18), (12, -22)], 6)
    lift = lambda u, v: tuple(c + d for c, d in zip(at(u, v + 6), (2.5, 2.5, 2.5)))
    s.tube([lift(u, v) for u, v in grip], 3.4, EDGE)
    for a, b in (((-20, 25), (-13, 19)), ((9, -25), (16, -19))):
        s.tube([lift(*a), lift(*b)], 5.4, EDGE)
