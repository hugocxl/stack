from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface, browser_window

DESCRIPTION = "A browser with a sidebar and four content cells carries a forked bookmark ribbon over its top-right edge."


def draw(s):
    page = browser_window(s, 112, 78)
    page.stroke([(32, 1), (32, 63)], EDGE)
    page.rules(8, 52, [16], ink=EDGE)
    page.rules(8, 41, [13, 16, 11], gap=9)
    for x in (41, 76):
        for v in (8, 32):
            page.rect(x, v, 27, 20, 2, EDGE)

    tab = Surface(s, page.point(87, 57, -2), across=page.across)
    tab.plate([(0, 0), (11, 8), (22, 0), (22, 28), (0, 28)], 4, BOLD)
