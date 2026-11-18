from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "A laptop shows a large laboratory flask for a software trial and carries a plus badge for joining."


def draw(s):
    s.box(0, 0, 0, 98, 58, 5, 4)
    upright(s, rounded(0, 5, 98, 64, 4), 8, 8)
    glass = front_surface(s, angle=0, y=8)
    glass.frame(5, 10, 88, 53, 2, DETAIL)
    glass.outline([(43, 54), (55, 54), (55, 41), (65, 22), (62, 19), (36, 19),
                   (33, 22), (43, 41)], BOLD)
    glass.line([(39, 32), (59, 32)], EDGE)
    glass.oval(47, 26, 1.5, 1.5, DETAIL)
    glass.oval(54, 28, 1.3, 1.3, DETAIL)
    for y in (17, 24, 31):
        s.line([(12, y, 5), (86, y, 5)], DETAIL)
    s.face([(x, y, 5) for x, y in rounded(36, 38, 26, 12, 2)], DETAIL)
    badge(s, "plus", *glass.at(95, 59), 14)
