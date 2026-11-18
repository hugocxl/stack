from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A raised bed holds three seedlings and carries a plus badge at its front corner."


def seedling(s, x, y, z, height):
    s.line([(x, y, z), (x, y, z + height)], EDGE)
    for angle in (40, 192):
        dx, dy = cos(radians(angle)), sin(radians(angle))
        for spread in (-1, 1):
            s.line([(x, y, z + height - 4),
                    (x + 5*dx - spread*dy*2, y + 5*dy + spread*dx*2, z + height + 3),
                    (x + 12*dx, y + 12*dy, z + height + 6)], EDGE)


def draw(s):
    s.box(-36, -24, 0, 72, 48, 13, 2)
    s.box(-32, -20, 12, 64, 40, 2, 2)
    for x in (-18, 0, 18):
        s.line([(x, 24, 2), (x, 24, 10)], DETAIL)
    for x, y, h in ((14, -10, 16), (-17, 1, 19), (6, 10, 17)):
        s.ellipse(x, y, 14, 5.3, 4.2, DETAIL)
        seedling(s, x, y, 14, h)
    badge(s, "plus", 34, 18, 9, 12)
