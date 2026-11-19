from geometry import EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A three-tier database cylinder carries a check badge on its upper corner."


def draw(s):
    s.solid(oval(27, 25, 27, 24)[:-1], 0, 47, crease=False)
    s.ellipse(27, 25, 47, 27, 24, EDGE)
    for z in (15.7, 31.3):
        s.ellipse(27, 25, z, 27, 24, EDGE, -42, 138)
    badge(s, "check", 48, 11, 45, 12.5)
