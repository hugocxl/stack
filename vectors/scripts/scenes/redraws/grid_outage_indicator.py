from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A lattice transmission pylon carries sagging power lines and a slash badge."


def draw(s):
    for y in (-7, 7):
        s.line([(-15, y, 0), (-7, y, 48), (-5, y, 80), (0, y, 90),
                (5, y, 80), (7, y, 48), (15, y, 0)], EDGE)
    for z, span in ((4, 14.4), (24, 11), (46, 7.4)):
        s.line([(-span, 7, z), (span, 7, z), (span, -7, z)], DETAIL)
    for side in (-1, 1):
        s.line([(side * 14.4, 7, 4), (side * -11, 7, 24),
                (side * 7.4, 7, 46)], DETAIL)
    for span, height in ((19, 76), (28, 58)):
        s.line([(-span, -7, height), (-span, 7, height), (-5, 7, height + 6),
                (5, 7, height + 6), (span, 7, height), (-span, 7, height)], EDGE)
        for x in (-span, span):
            s.line([(x, 7, height), (x, 7, height - 6)], EDGE)
        s.line([(span, 7 - 30*t/24, height - 6 - 28*(t/24)*(1-t/24))
                for t in range(25)], EDGE)
    badge(s, "slash", 28, -14, 65, 14)
