from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import outline

DESCRIPTION = "An open-padlock badge overlaps the monitor of a shared desk workstation."


def draw(s):
    for x, y in ((5, 4), (76, 4), (5, 44), (76, 44)):
        s.box(x, y, 0, 5, 5, 43, 1)
    s.box(0, 0, 42, 88, 53, 5, 4)
    s.box(24, 12, 47, 28, 18, 2, 3)
    s.box(35, 16, 49, 6, 6, 12, 1)
    s.box(7, 11, 60, 70, 8, 43, 4)
    outline(s, 12, 19, 67, 60, 30, 2, EDGE)
    for z, width in ((88, 31), (79, 23)):
        s.line([(18, 19, z), (18 + width, 19, z)], DETAIL)
    s.box(22, 35, 47, 43, 12, 2, 3)
    badge(s, "unlock", 80, 19, 101, 16)
