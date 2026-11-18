from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow

DESCRIPTION = "A broad circular arrow sweeps through a room panorama with a picture window."


def draw(s):
    wall = oval(0, 0, 47, 30, 148, 327, 56)
    s.face([(x, y, 0) for x, y in oval(0, 0, 47, 30, count=60)], EDGE)
    s.line([(x, y, -3) for x, y in oval(0, 0, 47, 30, 0, 180, 42)], DETAIL)
    s.face([(x, y, 49) for x, y in wall] + [(x, y, 0) for x, y in reversed(wall)], EDGE)
    x0, y0 = wall[0]
    x1, y1 = wall[-1]
    s.line([(x0, y0, 0), (x0, y0, 49)], EDGE)
    s.line([(x1, y1, 0), (x1, y1, 49)], EDGE)
    window = oval(0, 0, 46.5, 29.5, 207, 266, 24)
    for z in (18, 36):
        s.line([(x, y, z) for x, y in window], EDGE)
    for i in (0, 12, 24):
        x, y = window[i]
        s.line([(x, y, 18), (x, y, 36)], EDGE)
    arrow(s, [(x, y, 7) for x, y in oval(-3, 6, 34, 17, 306, 621, 64)],
          BOLD, head=8)
    s.box(9, -23, 0, 21, 10, 7, 2)
    s.box(9, -23, 7, 21, 4, 9, 1)
