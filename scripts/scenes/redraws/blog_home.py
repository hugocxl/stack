from geometry import BOLD, EDGE
from scenes.redraws._w2 import browser_page
from scenes.redraws._w4 import Surface, landscape

DESCRIPTION = "A browser window shows a lead blog article with a headline, thumbnail, and short excerpt."


def draw(s):
    at = browser_page(s, 108, 88, depth=9)
    browser = Surface(s, lambda u, v: at(u, 88 - v))
    browser.rows(11, 27, (69,), ink=BOLD)
    browser.rows(11, 36, (37,), ink=EDGE)
    landscape(browser, 11, 45, 33, 28)
    browser.rows(52, 48, (44, 38, 44, 30), step=7)
