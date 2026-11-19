from geometry import BOLD, EDGE
from scenes.redraws._w3 import reader_page

DESCRIPTION = "A double-headed vertical arrow spans the gap between text lines on a reading folio."


def draw(s):
    page = reader_page(s)
    page.rules(11, 52, [34, 33, 27], gap=22, ink=EDGE)
    place = page.viewer_axes(58, 34)
    for sign in (-1, 1):
        page.stroke([place(-6, 13.5 * sign), place(6, 13.5 * sign)], EDGE)
        page.stroke([place(-4.5, 6 * sign), place(0, 10.5 * sign),
                     place(4.5, 6 * sign)], BOLD)
    page.stroke([place(0, -10.5), place(0, 10.5)], BOLD)
