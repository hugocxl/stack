from geometry import BOLD, EDGE
from scenes.redraws._w3 import clipboard

DESCRIPTION = "A clipboard presents three widely spaced instructions with a growing count of dots beside each step."


def draw(s):
    page = clipboard(s, w=91, h=91)
    for count, v in enumerate((63, 43, 23), 1):
        page.rect(11, v - 7, 27, 14, 4, EDGE)
        for i in range(count):
            page.oval(24.5 + (i - (count - 1) / 2) * 7, v, 1.7, 1.7, BOLD)
        page.rules(46, v + 3, [31, 23], gap=6, ink=EDGE)
