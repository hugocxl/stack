from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface

DESCRIPTION = "A freestanding service kiosk has a tilted touchscreen and a card inserted into its payment slot."


def draw(s):
    s.box(-5, -10, 0, 57, 46, 6, 4)
    s.box(4, -2, 6, 39, 27, 51, 3)
    front = Surface(s, lambda u, v: (u, 25, v))
    front.frame(10, 31, 28, 7, 2, EDGE)
    card = Surface(s, lambda u, v: (u, 25 + v, 35 - .41*v))
    card.slab([(14, 0), (34, 0), (34, 12), (14, 12)], 2)
    card.line([(16, 9), (32, 9)], DETAIL)

    screen = Surface(s, lambda u, v: (u, 33 - .61*v, 51 + .79*v))
    screen.slab(rounded(-6, 0, 60, 62, 5), 10)
    screen.frame(0, 6, 48, 48, 3, EDGE)
    screen.rows(8, 43, (22,), ink=EDGE)
    for u in (8, 26):
        screen.frame(u, 23, 14, 13, 2)
    screen.frame(13, 11, 22, 6, 3, EDGE)
