from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import coin
from scenes.redraws._w4 import Surface, landscape

DESCRIPTION = "A microfilm reader feeds film from an exposed reel into a viewer showing a newspaper page."


def draw(s):
    s.box(0, 0, 0, 108, 52, 14, 5)
    s.box(38, 1, 14, 70, 44, 78, 7)
    screen = Surface(s, lambda u, v: (u, 45, 92 - v))
    screen.frame(43, 8, 60, 58, 4, EDGE)
    screen.frame(53, 14, 40, 46, 1)
    screen.rows(57, 21, (29,), ink=BOLD)
    landscape(screen, 57, 30, 14, 15)
    screen.rows(76, 32, (12, 11, 12, 9), step=4)
    screen.rows(57, 51, (30, 24), step=4)
    screen.rows(52, 72, (24,))
    screen.rows(86, 72, (7,))
    film = Surface(s, lambda u, v: (u, 46, v))
    film.frame(30, 9, 38, 14, 2, EDGE)
    film.rows(35, 16, (28,), ink=EDGE)
    s.box(3, 28, 14, 23, 13, 48, 4, DETAIL)
    for offset in (-2, 2):
        film.line([(17 + offset, 37), (24 + offset, 30), (33 + offset, 23),
                   (40 + offset, 16)], EDGE)
    spindle_x, spindle_z = 16, 54
    coin(s, spindle_x, 49, spindle_z, 21, depth=5)
    reel = Surface(s, lambda u, v: (u, 49, v))
    reel.oval(spindle_x, spindle_z, 4, 4, EDGE)
    for a in (30, 150, 270):
        x = spindle_x + 11.5*cos(radians(a))
        z = spindle_z + 11.5*sin(radians(a))
        reel.oval(x, z, 5, 5, EDGE)
