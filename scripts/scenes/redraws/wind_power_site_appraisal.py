from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import turbine

DESCRIPTION = "A wind turbine marker stands inside the outlined suitability zone on a raised terrain map."


def draw(s):
    def p(x, y):
        return (x, y, 8 - y * .53)

    s.face([p(-39, -28), p(39, -28), p(39, 28), p(-39, 28)], EDGE)
    s.face([p(-39, 28), p(39, 28), (39, 28, -11), (-39, 28, -11)], EDGE)
    s.face([p(39, -28), p(39, 28), (39, 28, -11), (39, -28, 18)], EDGE)
    for profile in (
        [(-38, -15), (-25, -9), (-21, 1), (-31, 12), (-32, 27)],
        [(-37, 2), (-32, 4), (-35, 13), (-36, 26)],
        [(38, -22), (25, -19), (18, -23), (8, -27)],
        [(38, -12), (29, -10), (31, 0), (38, 6)],
        [(2, 27), (8, 20), (18, 17), (30, 20), (37, 24)],
    ):
        s.line([p(x, y) for x, y in profile], DETAIL)
    zone = [(-13, -15), (6, -18), (21, -10), (22, 8), (12, 15),
            (-8, 16), (-19, 6), (-13, -15)]
    s.line([p(x, y) for x, y in zone], BOLD)
    turbine(s, 0, 4.8, 8, 37)
