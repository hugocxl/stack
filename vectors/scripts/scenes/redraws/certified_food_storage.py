from geometry import DETAIL
from scenes.redraws._kit import badge

DESCRIPTION = "A commercial refrigerator has a pull handle, a vented base, and a check badge on its door."


def draw(s):
    for x, y in ((5, 4), (39, 4), (5, 27), (39, 27)):
        s.box(x, y, 0, 4, 4, 5, 1)
    s.box(0, 0, 4, 48, 34, 65, 3)
    s.box(1, 33, 14, 46, 4, 53, 2.5)
    s.tube([(8, 37, 29), (8, 40, 29), (8, 40, 47), (8, 37, 47)], 1.3)
    for z in (7, 10, 13):
        s.line([(9, 34, z), (39, 34, z)], DETAIL)
    badge(s, "check", 43, 38, 51, 12)
