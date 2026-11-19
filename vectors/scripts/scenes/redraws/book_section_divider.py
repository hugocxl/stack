from geometry import BOLD, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open book has a bold ornamental flourish separating two blocks of text on its right page."


def draw(s):
    left, right = open_book(s)
    left.rows(13, 13, (40, 36, 42, 40, 36, 41, 33, 38, 27), step=5.5)
    right.rows(72, 12, (33,), ink=EDGE)
    right.rows(72, 20, (42, 39, 31), step=6)
    right.outline([(86, 43), (93, 36), (100, 43), (93, 50)], BOLD)
    right.line([(73, 40), (78, 43), (86, 43)], BOLD)
    right.line([(100, 43), (108, 43), (113, 40)], BOLD)
    right.rows(72, 56, (40, 38, 27), step=6)
