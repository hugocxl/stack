from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A slide on a pull-down presentation screen is framed by four fullscreen corners."


def draw(s):
    screen = Surface(s, (0, 0, 9), across=(.96, -.28))
    screen.plate(rounded(0, 0, 110, 68, 2), 2)
    s.tube([screen.point(-4, 68), screen.point(114, 68)], 3.6)
    s.tube([screen.point(0, 0), screen.point(110, 0)], 1.6)
    screen.stroke([(55, 0), (55, -6)], EDGE)
    screen.oval(55, -9, 3, 3, EDGE)
    photo_art(screen, 23, 16, 36, 35)
    screen.rules(66, 46, [20], ink=EDGE)
    screen.rules(66, 35, [17, 21, 13], gap=7)
    for x, dx in ((9, 1), (101, -1)):
        for v, dy in ((8, 1), (60, -1)):
            screen.stroke([(x + 11 * dx, v), (x, v), (x, v + 11 * dy)], BOLD)
