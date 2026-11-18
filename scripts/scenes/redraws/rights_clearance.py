from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A rubber approval stamp rests on a clearance slip and carries a check badge."


def draw(s):
    s.box(0, 5, 0, 110, 72, 2, 3, DETAIL)
    for y, width in ((17, 24), (25, 19), (49, 26), (58, 20)):
        s.line([(8, y, 2), (8 + width, y, 2)], DETAIL)

    s.box(37, 16, 2, 60, 48, 8, 5)
    s.box(34, 14, 10, 66, 52, 13, 6)
    x, y = 67, 39
    s.solid(oval(x, y, 18, 15)[:-1], 23, 21, top=oval(x, y, 9, 8)[:-1])
    s.solid(oval(x, y, 9, 8)[:-1], 44, 10, top=oval(x, y, 16, 13)[:-1])
    s.disk(x, y, 54, 18, 15, 9, EDGE)
    badge(s, "check", 100, 46, 20, 17)
