from geometry import BOLD, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open reference book pairs short bold headwords with ruled definitions and has thumb tabs along its outer edge."


def draw(s):
    left, right = open_book(s, tabs=True)
    for page, start in ((left, 11), (right, 73)):
        for v, length in ((12, 13), (32, 18), (52, 11)):
            page.rows(start, v, (length,), ink=BOLD)
            page.rows(start + length + 4, v, (25 - length/2,), ink=EDGE)
            page.rows(start, v + 6.5, (37, 28), step=5)
