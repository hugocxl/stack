from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "An arrow pairs equal-length ruler scales with coarse and fine divisions on one measurement card."


def draw(s):
    s.box(0, 0, 0, 110, 63, 6, 5)
    for y, count in ((15, 1), (47, 10)):
        s.line([(11, y, 6), (99, y, 6)], BOLD)
        for tick in range(count + 1):
            x = 11 + tick * 88 / count
            length = 6 if tick in (0, count) else 4.5 if tick == 5 else 3
            s.line([(x, y - length, 6), (x, y, 6)], EDGE)
    for x in (11, 99):
        s.line([(x, 17, 6), (x, 39, 6)], DETAIL, dashed=True)
    arrow(s, [(55, 20, 6), (55, 36, 6)], BOLD, head=6)
