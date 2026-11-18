from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A slash badge sits beside the dripping spout of an outdoor tap."


def draw(s):
    s.disk(-17, 0, 0, 9, 9, 4)
    s.disk(-17, 0, 4, 5, 5, 35)
    s.tube([(-17, 0, 35), (-12, 0, 44), (-3, 0, 48), (12, 0, 48),
            (19, 0, 44), (20, 0, 36)], 5.1, EDGE)
    s.disk(20, 0, 33, 6.6, 6.6, 5)
    s.disk(-4, 0, 52, 4, 4, 10)
    s.tube([(-15, 0, 62), (7, 0, 62)], 2.7, EDGE)
    s.tube([(-4, -9, 62), (-4, 9, 62)], 2.7, EDGE)
    s.line([(20, 0, 31), (15.8, 0, 25), (15.4, 0, 22), (17, 0, 19),
            (20, 0, 18), (23, 0, 19), (24.6, 0, 22), (24.2, 0, 25), (20, 0, 31)], EDGE)
    badge(s, "slash", 36, 0, 31, 11.5)
