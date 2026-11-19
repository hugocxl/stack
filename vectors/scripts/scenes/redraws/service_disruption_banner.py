from geometry import EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A freestanding status banner has an attached warning triangle beside two message lines."


def draw(s):
    for x in (7, 92):
        s.box(x, 0, 0, 12, 16, 4, 2)
        s.box(x + 3, 4, 4, 6, 8, 29, 2)
    front = front_surface(s, angle=0, y=15, z=25, lean=.30)
    front.slab(rounded(0, 0, 110, 38, 5), 7)
    front.rows(37, 24, (50,), ink=EDGE)
    front.rows(37, 13, (35,))
    warning(s, *front.at(17, 6), size=30)
