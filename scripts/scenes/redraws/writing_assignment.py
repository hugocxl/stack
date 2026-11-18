from geometry import EDGE
from scenes.redraws._w3 import pen_on, spiral_notebook

DESCRIPTION = "A fountain pen rests across the ruled lines of an open spiral notebook."


def draw(s):
    page = spiral_notebook(s, w=70, h=80)
    page.rules(16, 65, [35], ink=EDGE)
    page.rules(16, 53, [43, 37, 40, 44, 31], gap=9)
    pen_on(page, 31, 12, 62)
