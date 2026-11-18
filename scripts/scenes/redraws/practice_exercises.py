from geometry import EDGE
from scenes.redraws._w3 import clipboard

DESCRIPTION = "A practice worksheet on a clipboard has a short prompt above three open answer boxes."


def draw(s):
    page = clipboard(s, 91, 79)
    page.rules(15, 55, [35], ink=EDGE)
    page.rules(15, 44, [55, 43], gap=6)
    for x in (15, 38, 61):
        page.rect(x, 13, 15, 14, 2, EDGE)
