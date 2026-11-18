from geometry import EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "An author profile card shows a framed fountain pen nib above two short byline rows."


def draw(s):
    card = paper(s, 98, pitch=.84, run=.48, angle=-20, depth=7)
    card.slab(rounded(0, 0, 74, 98, 5), 7)
    card.frame(29, 6, 16, 4, 2, EDGE)
    card.frame(11, 16, 52, 47, 4)
    card.outline([(37, 22), (25, 39), (30, 55), (44, 55), (49, 39)], EDGE)
    card.line([(37, 22), (37, 39)], EDGE)
    card.oval(37, 42, 3, 3, EDGE)
    card.rows(17, 74, (40,), ink=EDGE)
    card.rows(24, 84, (26,))
