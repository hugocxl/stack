from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A single breadcrumb strip leads from a home through a folder to a page, separated by two chevrons."


def draw(s):
    strip = front_surface(s, angle=7, z=10, lean=.21)
    strip.slab(rounded(0, 0, 113, 35, 6), 8)
    for x in (36, 72):
        strip.line([(x, 0), (x + 9, 17.5), (x, 35)], EDGE)
    strip.outline([(12, 16), (12, 10), (25, 10), (25, 16),
                   (28, 16), (18.5, 25), (9, 16)], EDGE)
    strip.line([(17, 10), (17, 15), (20, 15), (20, 10)])
    strip.outline([(48, 11), (65, 11), (65, 21), (56, 21),
                   (54, 24), (48, 24)], EDGE)
    strip.outline([(87, 9), (101, 9), (101, 20), (95, 26), (87, 26)], BOLD)
    strip.line([(95, 26), (95, 20), (101, 20)], EDGE)
    strip.rows(90, 13, (8,))
