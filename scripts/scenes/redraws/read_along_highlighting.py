from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.line_focus_aid import reading_book

DESCRIPTION = "An open book highlights one word beside a speaker pictogram attached to its margin."


def draw(s):
    left, right = reading_book(s)
    left.rules(7, 54, [27, 23, 28, 24, 26], gap=8)
    right.rules(8, 54, [27, 23], gap=8)
    right.rules(8, 37, [7], ink=EDGE)
    right.rect(18, 33, 16, 8, 1.5, EDGE)
    right.rules(21, 37, [10], ink=BOLD)
    right.rules(37, 37, [6], ink=EDGE)
    right.rules(8, 26, [27, 30], gap=8)

    tab = Surface(s, right.point(0, 0, 1), rise=right.rise, back=right.back)
    tab.plate(rounded(41, 27, 25, 20, 3), 2)
    tab.stroke([(47, 35), (50, 35), (54, 32), (54, 42),
                (50, 39), (47, 39)], EDGE, closed=True)
    for radius in (4, 7):
        tab.stroke(oval(54, 37, radius, radius, -48, 48, 12), BOLD)
