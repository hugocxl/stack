from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface, browser_window, printed_glyph

DESCRIPTION = "An arrow curves from a closing dialog back to the doubly outlined button on the browser page beneath it."


def draw(s):
    page = browser_window(s, 110, 83)
    page.rules(10, 58, [42], ink=EDGE)
    page.rules(10, 47, [31, 23], gap=7)
    page.rect(67, 8, 33, 17, 4, EDGE)
    page.rect(72, 12, 23, 9, 2, BOLD)

    dialog = Surface(s, page.point(22, 31, -6), across=page.across)
    dialog.plate(rounded(0, 0, 63, 31, 4), 5)
    printed_glyph(dialog, "x", 53, 22, 6, EDGE)
    dialog.rules(7, 21, [25], ink=EDGE)
    dialog.rules(7, 11, [34])

    route = [page.point(u, v, -8) for u, v in
             ((83, 50), (96, 49), (105, 44), (107, 38), (101, 30), (94, 27))]
    arrow(s, route, BOLD, head=9)
