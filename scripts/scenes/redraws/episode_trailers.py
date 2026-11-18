from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A square podcast cover shows headphones with a play badge overlapping its lower-right corner."


def draw(s):
    cover = paper(s, 91, pitch=.69, run=.54, angle=-20, depth=7)
    cover.slab(rounded(0, 0, 91, 91, 5), 7)
    cover.line([(5, 6), (5, 85)])
    for rx, ry in ((25, 29), (21, 24)):
        cover.line(oval(45, 51, rx, ry, 180, 360, count=38), EDGE)
    cover.frame(17, 50, 14, 23, 5, EDGE)
    cover.frame(59, 50, 14, 23, 5, EDGE)
    for u in (27, 63):
        cover.line([(u, 54), (u, 69)])
    badge(s, "play", *cover.at(88, 78), 14)
