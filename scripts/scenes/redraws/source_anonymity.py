from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "An identification card has a slash badge overlapping its fingerprint panel."


def draw(s):
    card = paper(s, 61, pitch=.51, angle=3, depth=5)
    card.slab(rounded(0, 0, 94, 61, 5), 5)
    card.frame(10, 8, 43, 44, 3, EDGE)
    for radius in (4, 8, 12, 16):
        points = oval(30, 29, radius, radius, 172, 359, 24)
        card.line([(30 - radius, 29 + radius*.71), *points, (30 + radius, 30 + radius*.66)], EDGE)
    card.rows(60, 17, (25, 20, 24, 17), step=8)
    badge(s, "slash", *card.at(45, 54), 15)
