from geometry import DETAIL, EDGE, oval

DESCRIPTION = "A raised curb separates a painted bicycle lane from the road beside it."


def draw(s):
    s.box(-60, -56, 0, 120, 112, 2, 1)
    s.box(-60, -4, 2, 120, 8, 7, 3)
    for x in range(-56, 60, 20):
        s.line([(x, 30, 2), (x + 10, 30, 2)], DETAIL)
    p = lambda u, v: (u*1.5, -30 + v*1.5, 2.01)
    for cx in (-14, 14):
        s.line([p(cx + a, b) for a, b in oval(0, 0, 9, 9, count=36)], EDGE)
    s.line([p(-14, 0), p(-2, -9), p(10, -9), p(14, 0)], EDGE)
    s.line([p(-2, -9), p(2, 0), p(10, -9)], EDGE)
    s.line([p(-5, -12), p(1, -12)], EDGE)
    s.line([p(10, -9), p(9, -13), p(13, -13)], EDGE)
