from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge


DESCRIPTION = "A building permit certificate shows a house outline and a checkmark seal."


def draw(s):
    y = 0
    s.face([(0, y, 0), (76, y, 0), (76, y, 63), (64, y, 75), (0, y, 75)], EDGE)
    s.line([(64, y, 75), (64, y, 63), (76, y, 63)], DETAIL)
    s.line([(13, y, 44), (37, y, 68), (61, y, 44)], EDGE)
    s.line([(19, y, 50), (19, y, 29), (55, y, 29), (55, y, 50)], EDGE)
    s.line([(33, y, 29), (33, y, 42), (42, y, 42), (42, y, 29)], EDGE)
    s.line([(13, y, 20), (43, y, 20)], DETAIL)
    s.line([(13, y, 12), (35, y, 12)], DETAIL)
    badge(s, "check", 67, 3, 13, 15)
