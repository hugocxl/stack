from geometry import EDGE
from scenes.redraws._w3 import book, pen_on

DESCRIPTION = "A bound timeline shows three event ticks and a pencil touching the newest entry."


def draw(s):
    page = book(s, w=109, h=66, depth=10)
    page.rules(15, 60, [42], ink=EDGE)
    page.stroke([(15, 24), (98, 24)], EDGE)
    for x in (24, 50, 76):
        page.stroke([(x, 27), (x, 39)], EDGE)
        page.oval(x, 24, 3, 3, EDGE)
        page.rules(x - 7, 42, [14], ink=EDGE)
        page.rules(x - 5, 48, [10])
    pen_on(page, 82, 42, length=39, pencil=True)
