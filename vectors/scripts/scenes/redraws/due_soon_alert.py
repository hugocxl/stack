from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import coin, glyph, warning

DESCRIPTION = "A two-bell alarm clock carries an exclamation triangle on its lower rim."


def draw(s):
    for side in (-1, 1):
        s.tube([(side*12, -3, 12), (side*18, 0, 2)], 2.5, EDGE)
        x, y = side*15, -3
        s.tube([(x*.79, y, 46), (x, y, 51)], 2)
        s.solid(oval(x, y, 8.5, 7, count=32)[:-1], 50, 6,
                top=oval(x, y, 4, 3.8, count=32)[:-1], crease=False)
    coin(s, 0, 0, 29, 25, 8)
    for x, z, dx, dz in ((0, 49, 0, -3), (0, 9, 0, 3),
                         (20, 29, -3, 0), (-20, 29, 3, 0)):
        s.line([(x, 0, z), (x + dx, 0, z + dz)], DETAIL)
    glyph(s, "clock", 0, 0, 29, 18, BOLD)
    warning(s, 27.5, 1, 7, 27)
