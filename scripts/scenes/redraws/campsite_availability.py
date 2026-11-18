from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A pitched A-frame tent with an open entry carries a check badge near the back of its roof."


def draw(s):
    left, peak, right = (0, 48, 0), (26, 48, 39), (52, 48, 0)
    rear_peak, rear_right = (26, 0, 39), (52, 0, 0)
    s.face([left, peak, right], EDGE)
    s.face([peak, rear_peak, rear_right, right], EDGE)
    s.face([(10, 48, 0), (26, 48, 28), (43, 48, 0)], EDGE)
    s.line([(26, 48, 28), (26, 48, 2)], DETAIL)
    s.line([(31, 42, 31.5), (31, 6, 31.5)], DETAIL)
    badge(s, "check", 43, 6, 39, 12)
