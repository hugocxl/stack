from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import memory_chip

DESCRIPTION = "A small open wastebasket catches a square allocation beside a pin-legged memory chip."


def draw(s):
    memory_chip(s)

    x, y, bottom, h, radius = 41, 8, 0, 29, 14
    foot = oval(x, y, 9.5, 9.5)[:-1]
    top = oval(x, y, radius, radius)[:-1]
    s.solid(foot, bottom, h, top=top, crease=False)
    s.ellipse(x, y, h, radius, radius, EDGE)
    s.ellipse(x, y, h, radius - 3, radius - 3, DETAIL)
    s.box(x - 3, y - 6, h - 2, 8, 8, 7, 1)
    s.ellipse(x, y, h, radius, radius, EDGE, start=-45, end=135)
    for angle in (14, 59, 104):
        a, b = oval(0, 0, 1, 1, angle, angle, 1)[0]
        s.line([(x + 8.5 * a, y + 8.5 * b, 5),
                (x + 12.8 * a, y + 12.8 * b, 22)], DETAIL)
