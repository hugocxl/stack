from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._sf import BACK, gear, ground, plate, screen

DESCRIPTION = "A raw cube, a gear and a check seal stand in a row, joined by two arrows."


def arrow(s, x0, x1):
    s.line([(x0, -x0*0 + 0, 0), (x1, 0, 0)], EDGE)


def draw(s):
    at = screen()
    s.box(-104, -18, 0, 34, 34, 34, 3)
    g = lambda u, v: at(u, v + 20)
    plate(s, g, gear(28, 10), 9, BACK)
    s.line([g(a, b) for a, b in oval(0, 0, 9, 9, count=32)], EDGE)
    c = lambda u, v: at(u + 92, v + 20)
    plate(s, c, oval(0, 0, 24, 24, count=64)[:-1], 7, BACK)
    for stroke in _strokes("check", 14):
        s.line([c(u, v) for u, v in stroke], BOLD)
    for u0, u1 in ((-58, -38), (38, 58)):
        s.line([at(u0, 20), at(u1, 20)], EDGE)
        s.line([at(u1 - 5, 25), at(u1, 20), at(u1 - 5, 15)], EDGE)
