from geometry import EDGE
from scenes.redraws._w3 import Surface, sheet, speech_outline

DESCRIPTION = "A document carries one anchored speech bubble with two rows of visibly different scripts."


def draw(s):
    page = sheet(s, 75, 78, rise=(-.49, .87), depth=6)
    page.rules(10, 62, [36], ink=EDGE)
    page.rules(10, 51, [32, 52, 46, 52, 29], gap=8)

    bubble = Surface(s, page.point(31, 28, -5), rise=page.rise, back=page.back)
    bubble.plate(speech_outline(0, 0, 70, 47), 4)
    for x in (15, 30, 46):
        bubble.stroke([(x, 30), (x+4, 39), (x+8, 30)], EDGE)
        bubble.rules(x + 2, 33, [4], ink=EDGE)
    bubble.stroke([(15, 17), (20, 14), (25, 15), (27, 19), (27, 14), (34, 14),
                   (38, 20), (38, 15), (46, 14), (51, 17), (52, 22)], EDGE)
    bubble.rules(42, 21, [2], ink=EDGE)
