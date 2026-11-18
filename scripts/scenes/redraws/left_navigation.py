from geometry import BOLD, EDGE
from scenes.redraws._w3 import browser_window, photo_art

DESCRIPTION = "A browser window has a bounded left navigation sidebar with one outlined row and a page preview to its right."


def draw(s):
    page = browser_window(s, 117, 77)
    page.stroke([(44, 0), (44, 62)], EDGE)
    page.rect(5, 43, 34, 13, 3, BOLD)
    for z in (49.5, 34, 24, 14):
        page.rect(10, z - 2, 4, 4, .8, EDGE)
        page.rules(19, z, [15 if z != 24 else 11], ink=EDGE)
    photo_art(page, 57, 25, 47, 27)
    page.rules(57, 17, [43, 29], gap=6)
