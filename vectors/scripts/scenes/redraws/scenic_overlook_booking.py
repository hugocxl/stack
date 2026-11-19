from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A wooden overlook deck with a railing faces a continuous mountain ridge and carries a clock badge."


def draw(s):
    s.face([(-22, 6, 5), (-19, 6, 19), (-8, 6, 31), (3, 6, 27), (22, 6, 56),
            (37, 6, 37), (45, 6, 43), (61, 6, 23), (70, 6, 8), (70, 6, 2)], EDGE)
    s.line([(13, 6, 42), (18, 6, 39), (23, 6, 45),
            (29, 6, 40), (34, 6, 41)], DETAIL)

    for x, y in ((3, 18), (42, 18), (3, 51), (42, 51)):
        s.box(x, y, 0, 4, 4, 10, .8)
    s.box(0, 15, 9, 50, 43, 4.5, 2)
    for y in (27, 36, 45, 54):
        s.line([(2, y, 13.5), (48, y, 13.5)], DETAIL)
    for x, y in ((2, 17), (23, 17), (45, 17), (45, 32), (45, 54), (2, 32)):
        s.box(x, y, 13.5, 2.4, 2.4, 14, .55)
    s.box(1, 16, 26, 48, 4, 2.4, .7)
    s.box(44.5, 19, 26, 4.5, 37, 2.4, .7)
    s.box(1, 19, 26, 4.2, 15, 2.4, .7)
    badge(s, "clock", 58, 22, 30, 11)
