from geometry import DETAIL, EDGE
from scenes.redraws._sf import ground, plate, smooth, squircle

DESCRIPTION = "A thick gift card is wrapped in a crossed ribbon tied in a two-loop bow."


def draw(s):
    w, d, h = 100, 64, 5
    top = ground(-w/2, -d/2, h)
    plate(s, top, squircle(w, d, 8), h, (0, 0, -1))
    rx, ry = 62, 40
    for u in (rx - 4, rx + 4):
        s.line([top(u, 0), top(u, d)], EDGE)
    for v in (ry - 4, ry + 4):
        s.line([top(0, v), top(w, v)], EDGE)
    # Two loops and two tails, drawn as smooth closed curves around the knot.
    for loop in ([(0, 0), (-10, 9), (-22, 10), (-24, 1), (-12, -3)], [(0, 0), (10, 9), (22, 10), (24, 1), (12, -3)]):
        pts = smooth(loop, 8, closed=True)
        s.face([top(rx + a, ry + b, ) for a, b in pts], EDGE)
    for tail in ([(-2, -2), (-8, -12), (-6, -20)], [(2, -2), (8, -12), (6, -20)]):
        s.line([top(rx + a, ry + b) for a, b in smooth(tail, 6)], EDGE)
    knot = [top(rx + a, ry + b) for a, b in squircle(6, 6, 2.5)]
    s.face([(x - 3, y - 3, z) for x, y, z in knot], EDGE)
