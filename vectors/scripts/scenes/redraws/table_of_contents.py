from geometry import EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open book shows a chapter list with dotted leaders and aligned page references."


def draw(s):
    left, right = open_book(s)
    left.rows(12, 17, (40,), ink=EDGE)
    for v, width in ((32, 12), (43, 19), (54, 9), (65, 16)):
        left.rows(12, v, (width,), ink=EDGE)
        for u in range(14 + width, 46, 5):
            left.rows(u, v, (1.8,), ink=EDGE)
        left.rows(48, v, (6,), ink=EDGE)
    right.rows(78, 24, (31,), ink=EDGE)
    right.rows(75, 36, (34, 38, 33, 24), step=7)
