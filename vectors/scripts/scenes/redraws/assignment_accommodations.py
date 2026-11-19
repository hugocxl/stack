from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import flat

DESCRIPTION = "A school desk holds a worksheet above telescoping legs and an up-arrow badge."


def draw(s):
    for x in (8, 73):
        s.box(x - 3, 3, 0, 13, 51, 5, 3)
        s.box(x, 24, 4, 8, 10, 34, 1)
        s.box(x + 1.5, 25.5, 38, 5, 7, 22, 1)
        for z in (47, 52):
            s.line([(x + 3, 32.5, z), (x + 5, 32.5, z)], EDGE)
    s.box(5, 11, 52, 84, 31, 9, 2)
    s.box(0, 0, 61, 96, 56, 5, 5)
    page = flat(s, 20, 49, 67)
    page.rect(0, 0, 48, 36, 2, EDGE)
    page.rules(7, 28, [23], ink=EDGE)
    page.rules(7, 19, [31, 27, 30], gap=6)
    badge(s, "up", 87, 19, 31, 13)
