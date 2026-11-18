from geometry import EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "A ribbon bookmark crosses an open book and hangs in a notched tail below the current spread."


def draw(s):
    left, right = open_book(s)
    for page, u in ((left, 12), (right, 81)):
        page.rows(u, 15, (32,), ink=EDGE)
        page.rows(u, 25, (36, 29, 35, 34, 23, 30), step=6)
    start, end = 63, 77
    s.face([right.at(start, 11), right.at(end, 11), right.at(end, 72),
            (end, 97, 5), (70, 91, 6), (start, 97, 5), right.at(start, 72)])
