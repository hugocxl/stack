from geometry import BOLD, DETAIL, EDGE, GUIDE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A reading band frames one crisp line on an open book while its neighboring lines fade."


def reading_book(s):
    """An open book resting on its covers, with a shallow valley at the spine."""
    left = Surface(s, (0, 62, 5), rise=(-.63, .67), back=(0, -.67, -.63))
    right = Surface(s, left.point(41, 0), rise=left.rise, back=left.back)
    left.plate([(0, 2), (9, 0), (36, 1), (41, 6), (41, 68), (35, 72), (8, 71), (0, 68)], 6)
    right.plate([(0, 6), (7, 3), (37, 5), (47, 2), (47, 68),
                 (39, 72), (8, 71), (0, 68)], 6)
    left.stroke([(4, 5), (35, 4), (39, 7)], DETAIL)
    right.stroke([(5, 7), (38, 11), (43, 9)], DETAIL)
    return left, right


def draw(s):
    left, right = reading_book(s)
    left.rules(7, 54, [27, 23, 28, 24, 26], gap=8, ink=GUIDE)
    right.rules(8, 55, [30, 24], gap=8, ink=GUIDE)
    right.rect(5, 31, 38, 12, 1.5, EDGE)
    right.rules(9, 37, [29], ink=BOLD)
    right.rules(8, 25, [27, 31], gap=8, ink=GUIDE)
