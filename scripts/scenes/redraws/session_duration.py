from math import cos, radians, sin

from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import coin

DESCRIPTION = "A stopwatch shows elapsed time with a strong arc from twelve o’clock to the tip of its hand."


def draw(s):
    s.box(-7, -6, 82, 14, 11, 8, 2)
    s.box(-11, -8, 89, 22, 15, 7, 3)
    s.tube([(26, -3, 71), (33, -3, 78)], 3.4)
    front = coin(s, 0, 7, 43, 43, depth=9)
    for a in range(0, 360, 30):
        u, v = cos(radians(a)), sin(radians(a))
        s.line([(u * r, front, 43 + v * r) for r in (29, 33)], EDGE)
    elapsed = -26
    for radius, ink in ((23, BOLD), (26.5, EDGE)):
        s.line([(x, front, z) for x, z in oval(0, 43, radius, radius, elapsed, 90, 34)], ink)
    s.line([(0, front, 66), (0, front, 69.5)], EDGE)
    u, v = cos(radians(elapsed)), sin(radians(elapsed))
    s.line([(0, front, 43), (u * 26.5, front, 43 + v * 26.5)], BOLD)
    s.line([(x, front, z) for x, z in oval(0, 43, 3, 3, count=22)], EDGE)
