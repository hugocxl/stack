from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, browser_window

DESCRIPTION = "A blank brand plate slides into a recessed logo holder on a browser masthead."


def draw(s):
    page = browser_window(s, 111, 77)
    page.rect(9, 38, 48, 16, 3, EDGE)
    page.rules(12, 42, [42])
    page.stroke([(48, 46), (51, 49), (54, 46), (51, 43)], EDGE, closed=True)
    page.rules(70, 46, [14, 26], gap=6)
    page.stroke([(1, 32), (110, 32)])
    page.rect(10, 7, 39, 19, 2)
    page.rules(58, 22, [38, 31, 36], gap=6)
    label = Surface(s, page.point(-7, 42, -5), across=page.across)
    label.plate(rounded(0, 0, 51, 12, 2), 4)
