from geometry import BOLD, EDGE
from scenes.redraws._w4 import open_book, printed_glyph

DESCRIPTION = "An open history book highlights the first milestone on a timeline across its opening pages."


def draw(s):
    left, right = open_book(s)
    left.rows(13, 13, (34,), ink=EDGE)
    left.line([(12, 40), (18, 40)], EDGE)
    left.oval(28, 40, 9, 11, EDGE)
    printed_glyph(left, "star", 28, 40, 10, BOLD)
    left.line([(38, 40), (60, 40)], EDGE)
    left.rows(17, 54, (24, 16), step=6)
    right.rows(73, 13, (32,), ink=EDGE)
    for u in (75, 101):
        right.oval(u + 7, 40, 3, 4, EDGE)
        right.rows(u, 54, (13, 10), step=6)
    for start, end in ((66, 79), (86, 105), (111, 116)):
        right.line([(start, 40), (end, 40)], EDGE)
