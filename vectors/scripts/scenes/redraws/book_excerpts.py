from geometry import BOLD, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open book brackets a three-line passage on its right page."


def draw(s):
    left, right = open_book(s)
    left.rows(12, 13, (31,), ink=EDGE)
    left.rows(12, 23, (42, 37, 41, 39, 43, 35, 28), step=6)
    right.rows(72, 12, (40, 35), step=7)
    right.rows(77, 29, (29, 24, 29), step=7, ink=EDGE)
    right.rows(72, 56, (42, 35), step=7)
    for u, du in ((71, 1), (114, -1)):
        right.line([(u + du*4, 25), (u, 25), (u, 47), (u + du*4, 47)], BOLD)
