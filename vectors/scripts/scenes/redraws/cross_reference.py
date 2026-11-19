from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import bezier_path, open_book

DESCRIPTION = "A curved arrow connects two marked passages on opposite pages of an open reference book."


def draw(s):
    left, right = open_book(s)
    left.rows(13, 12, (28, 34), step=8)
    left.rows(13, 50, (35, 26, 33), step=7)
    right.rows(75, 12, (30, 36, 24), step=7)
    right.rows(77, 57, (32, 24), step=7)
    left.frame(12, 30, 30, 11, 2, EDGE)
    left.rows(17, 35.5, (20,), ink=EDGE)
    right.frame(89, 39, 26, 11, 2, EDGE)
    right.rows(93, 44.5, (18,), ink=EDGE)

    start = left.at(42, 35.5)
    end = right.at(85.5, 44.5)
    path = bezier_path(start, ((56, 20, 31), (74, 37, 27), end), count=24)
    arrow(s, path, BOLD, head=9)
