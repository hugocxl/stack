from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel

DESCRIPTION = "A garage floor plan shows a parked car and a lightning bolt badge marking a charging bay."


def draw(s):
    def floor(x, d):
        return x, -.65 * d, .55 * d

    panel(s, [(0, 0), (78, 0), (78, 65), (0, 65)], floor, 4)
    for lower, upper in ((3, 24), (43, 62)):
        s.line([floor(4, upper), floor(74, upper)], EDGE)
        for x in (4, 21, 38, 55, 74):
            s.line([floor(x, lower), floor(x, upper)], EDGE)
    for x in (8, 25, 42, 59):
        s.line([floor(x, 33), floor(x + 9, 33)], DETAIL)
    car = rounded(24, 5.5, 11, 16, 2.8)
    s.face([floor(x, d) for x, d in car], EDGE)
    for d in (10, 17):
        s.line([floor(24.5, d), floor(34.5, d)], DETAIL)
    badge(s, "bolt", *floor(64.5, 55), 11.5)
