from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.systems_shapes import rectangle

DESCRIPTION = "A bound recovery runbook shows three drill steps and a restore arrow."


def draw(s):
    s.box(-35, -42, 0, 70, 84, 8, 3)
    for y in range(-30, 32, 12):
        s.line([(x, y, z) for x, z in oval(-31, 8, 6, 4, 15, 305, 18)], EDGE)
    for y, width in ((-12, 35), (3, 28), (18, 33)):
        rectangle(s, -18, y, 8, 7, 7, EDGE, 1)
        s.line([(-4, y + 3.5, 8), (-4 + width, y + 3.5, 8)], EDGE)

    badge(s, "refresh", 32, -24, 12, 13)
