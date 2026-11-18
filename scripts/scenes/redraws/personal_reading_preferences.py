from geometry import BOLD, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open ebook pairs flowing text with a built-in control showing two sizes of the same letter."


def draw(s):
    left, right = open_book(s)
    left.rows(12, 18, (39,), ink=EDGE)
    left.rows(12, 30, (41, 35, 41, 26), step=8)
    right.frame(72, 17, 42, 30, 3, EDGE)
    for x, y, size in ((84, 35, 8), (101, 33, 13)):
        right.line([(x - size * .45, y + size / 2), (x, y - size / 2),
                    (x + size * .45, y + size / 2)], BOLD)
        right.line([(x - size * .25, y + size * .21),
                    (x + size * .25, y + size * .21)], BOLD)
    right.rows(77, 55, (34, 21), step=7)
