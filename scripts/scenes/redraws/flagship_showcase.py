from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A thick retail product box carries a prominent star badge on its front upper corner."


def draw(s):
    s.box(0, 0, 0, 67, 40, 70, 3)
    s.line([(0, 40, 53), (67, 40, 53), (67, 0, 53)], DETAIL)
    s.face([(13, 40, 13), (45, 40, 13), (45, 40, 41), (13, 40, 41)], DETAIL)
    s.line([(13, 40, 19), (45, 40, 19)], EDGE)
    s.line([(20, 40, 9), (38, 40, 9)])
    badge(s, "star", 59, 42, 56, 18)
