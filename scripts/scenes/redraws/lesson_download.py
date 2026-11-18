from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import clipboard

DESCRIPTION = "A lesson sheet on a standing clipboard has an open-book heading and a download badge."


def draw(s):
    page = clipboard(s, 79, 91)
    page.stroke([(19, 53), (19, 70), (29, 72), (40, 68), (51, 72), (61, 70),
                 (61, 53), (51, 54), (40, 50), (29, 54)], EDGE, closed=True)
    page.stroke([(40, 68), (40, 50)], EDGE)
    page.rules(20, 40, [39, 32, 36, 25], gap=8)
    badge(s, "down", *page.point(74, 13), 13)
