from geometry import EDGE
from scenes.redraws._w4 import closed_book, wrench_mark

DESCRIPTION = "A trade service contract booklet has a wrench seal on its cover above the terms and signature lines."


def draw(s):
    book = closed_book(s, angle=-5, width=73, height=91, depth=11)
    book.oval(55, 24, 12, 12, EDGE)
    wrench_mark(book, 55, 24, .34)
    book.rows(15, 23, (21,), ink=EDGE)
    book.rows(15, 43, (44, 47, 35), step=7)
    book.line([(15, 77), (59, 77)])
    book.line([(17, 72), (22, 64), (23, 73), (30, 69), (33, 71)], EDGE)
