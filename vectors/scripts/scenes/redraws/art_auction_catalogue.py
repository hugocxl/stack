from geometry import BOLD, EDGE
from scenes.redraws._w3 import book

DESCRIPTION = "A bound auction catalogue shows a gavel and sounding block on its cover."


def draw(s):
    cover = book(s, w=74, h=83, depth=14)
    cover.rules(17, 73, [46], ink=EDGE)
    cover.rules(17, 64, [31])
    cover.stroke([(20, 53), (27, 53), (28, 49), (43, 49), (44, 53), (51, 53),
                  (51, 34), (45, 34), (62, 15), (57, 11), (37, 34), (28, 34),
                  (27, 30), (20, 30)], BOLD, closed=True)
    for x in (27, 44):
        cover.stroke([(x, 47), (x, 36)], EDGE)
    cover.rect(21, 14, 20, 6, 1, EDGE)
