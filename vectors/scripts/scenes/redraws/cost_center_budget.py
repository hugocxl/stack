from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import coin_stack, printed_stroke, rect

DESCRIPTION = "An office block shares a base with a recessed coin tray and an allocation gauge."


def draw(s):
    s.box(0, 0, 0, 63, 43, 8, 3)
    s.box(2, 1, 8, 31, 27, 50, 1.5)
    s.box(1, 0, 56, 33, 29, 4, 1.2)
    face = lambda x, z: (x, 28, z)
    for z in (26, 38, 49):
        for x in (7, 20):
            rect(s, face, x, z - 3, 7, 6, .7, DETAIL)
    rect(s, face, 12, 8, 9, 10, .5, EDGE)
    gauge = lambda x, z: (x, 24, z)
    s.box(33, 3, 8, 25, 21, 30, 2)
    printed_stroke(s, gauge, oval(45.5, 24, 8.4, 9, 0, 180, 20), EDGE)
    printed_stroke(s, gauge, [(37, 24), (54, 24)], DETAIL)
    printed_stroke(s, gauge, [(45.5, 24), (50, 30)], EDGE)
    s.box(35, 26, 8, 25, 14, 2.2, 1.6)
    coin_stack(s, 48, 34, 10.2, 6.4, 3)
    s.box(35, 39, 10, 25, 2, 4, .8)
