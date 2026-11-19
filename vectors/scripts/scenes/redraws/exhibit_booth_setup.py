from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "A trade-show booth has a rectangular display sign sliding down into its upright mounting rails."


def draw(s):
    s.box(0, 0, 0, 92, 7, 77, 2)
    s.box(0, 4, 0, 6, 36, 72, 2)
    s.box(85, 3, 0, 7, 12, 94, 1)
    s.box(8, 4, 0, 5, 11, 94, 1)
    back = Surface(s, (0, 7, 0))
    back.rect(20, 46, 60, 40, 1, EDGE)
    s.box(23, 31, 0, 56, 28, 38, 2)
    counter = Surface(s, (23, 59, 0))
    counter.rect(6, 6, 44, 24, 2)
    sign = Surface(s, (0, 11, 0))
    sign.plate(rounded(17, 68, 64, 34, 2), 3)
    sign.rect(22, 74, 16, 21, 1, EDGE)
    sign.rules(44, 88, [29], ink=EDGE)
    sign.rules(44, 80, [21])
    s.box(11, 10, 44, 9, 5, 39, 1)
    s.box(78, 10, 44, 9, 5, 39, 1)
    arrow(s, [(109, 13, 108), (109, 13, 78)], BOLD, head=9)
