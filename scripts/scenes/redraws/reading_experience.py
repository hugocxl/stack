from geometry import EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open book shows two uninterrupted columns of print with a low gutter between them."


def draw(s):
    left, right = open_book(s)
    left.rows(11, 15, (44,), ink=EDGE)
    right.rows(72, 15, (36,), ink=EDGE)
    left.rows(11, 26, (42, 42, 43, 40, 41, 28), step=6.5)
    right.rows(72, 26, (42, 41, 43, 41, 43, 30), step=6.5)
