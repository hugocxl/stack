from geometry import BOLD, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import Surface

DESCRIPTION = "An office-hours ticket dispenser shows three queue slips with an arrow beside the first."


def draw(s):
    s.box(0, 0, 0, 85, 35, 47, 6)
    display = Surface(s, (0, 35, 0))
    display.rect(7, 20, 71, 20, 3, EDGE)
    for x in (29, 47, 65):
        display.rect(x - 5, 25, 10, 9, 1, EDGE)
        display.rules(x - 2, 29, [4])
    display.rect(17, 7, 51, 7, 2, BOLD)
    stub = Surface(s, (0, 38, 0))
    stub.plate([(28, 11), (57, 11), (57, -8), (53, -5), (48, -8),
                (43, -5), (38, -8), (33, -5), (28, -8)], 2)
    stub.rules(34, 4, [17], ink=EDGE)
    glyph(s, "arrow", 15, 35, 29.5, 6.4)
