from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A pagination strip has previous and next chevrons and three page buttons, with the current page double-outlined."


def draw(s):
    strip = front_surface(s, angle=-14, lean=.23, z=9)
    strip.slab(rounded(0, 0, 115, 35, 7), 8)
    strip.line([(14, 22), (9, 17.5), (14, 13)], EDGE)
    strip.line([(101, 22), (106, 17.5), (101, 13)], EDGE)
    for u in (34.5, 57.5, 80.5):
        strip.frame(u - 8, 9.5, 16, 16, 3, BOLD if u == 57.5 else EDGE)
    strip.frame(52.5, 12.5, 10, 10, 1.6, BOLD)
