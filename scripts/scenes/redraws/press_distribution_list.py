from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A press mailing list pairs three envelope-marked recipient rows with a send badge."


def draw(s):
    page = paper(s, 88, pitch=.43, angle=-6, depth=7)
    page.slab(rounded(0, 0, 91, 88, 3), 7)
    page.rows(12, 14, (41,), ink=BOLD)
    page.rows(12, 23, (64,), ink=EDGE)
    for row, width in ((33, 39), (50, 47), (67, 34)):
        page.frame(12, row, 15, 11, 1, EDGE)
        page.line([(13, row + 1), (19.5, row + 6), (26, row + 1)], EDGE)
        page.rows(34, row + 3, (width, width * .63), step=5)
    badge(s, "arrow", *page.at(93, 32), 16)
