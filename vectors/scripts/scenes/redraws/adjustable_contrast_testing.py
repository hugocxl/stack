from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A split contrast dial has a strong half and a faint half, with a short adjustment slider over its center."


def draw(s):
    dial = Surface(s, (0, 0, 0), rise=(-.39, .92), back=(0, -.92, -.39))
    dial.plate(oval(41, 42, 41, 42)[:-1], 13)
    dial.oval(41, 42, 33, 34, DETAIL)
    dial.stroke(oval(41, 42, 33, 34, 90, 270), BOLD)
    dial.stroke([(41, 8), (41, 76)], BOLD)
    dial.stroke(oval(41, 42, 24, 25, 90, 270), EDGE)
    slider = Surface(s, dial.point(0, 0, -3), rise=dial.rise, back=dial.back)
    slider.plate(rounded(17, 35, 50, 14, 5), 3, EDGE)
    slider.rules(23, 42, [38], ink=EDGE)
    slider.plate(rounded(42, 34, 11, 16, 4), 2, EDGE)
