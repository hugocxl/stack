from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, open_book

DESCRIPTION = "An open textbook holds a protruding exam sheet with three rows of answer bubbles."


def draw(s):
    left, right = open_book(s)
    left.rows(13, 18, (34,), ink=EDGE)
    left.rows(13, 29, (38, 38, 29, 36, 21), step=7)
    right.rows(78, 46, (32, 36, 25), step=8)

    def point(u, v):
        return (70 + u + v * .13, v - 13, 25 - v * .12)

    exam = Surface(s, point)
    exam.slab(rounded(0, 0, 53, 51, 2), 1, BOLD)
    exam.rows(8, 8, (34,), ink=EDGE)
    exam.rows(8, 20, (8, 8, 8), step=10, ink=DETAIL)
    for v in (20, 30, 40):
        for x in (24, 34, 44):
            exam.oval(x, v, 2.9, 2.9, EDGE)
