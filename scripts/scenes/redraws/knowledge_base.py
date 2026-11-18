from geometry import EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open reference book has three projecting index tabs and a bulleted contents spread."


def draw(s):
    left, right = open_book(s, tabs=True)
    left.rows(12, 15, (35,), ink=EDGE)
    for v, width in ((31, 29), (43, 33), (55, 24)):
        left.oval(14, v, 1.5, 1.5, EDGE)
        left.rows(21, v, (width,), ink=EDGE)
    right.rows(75, 15, (27,), ink=EDGE)
    right.rows(75, 30, (36, 30, 34, 27, 21))
