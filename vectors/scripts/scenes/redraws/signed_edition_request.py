from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open hardcover shows an autograph on its title page and carries a plus badge."


def draw(s):
    left, title = open_book(s)
    left.rows(14, 30, (29, 34, 27), step=8)
    title.rows(75, 16, (34,), ink=EDGE)
    title.rows(80, 24, (23,))
    title.line([(72, 58), (86, 44), (86, 41), (82, 42), (78, 51), (80, 54),
                (88, 49), (91, 53), (99, 47), (100, 51), (110, 47), (116, 47)], EDGE)
    title.rows(73, 61, (43,))
    badge(s, "plus", 124, 12, 19, 17)
