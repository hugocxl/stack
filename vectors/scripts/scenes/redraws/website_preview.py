from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, browser_window, preview_page, visibility_art

DESCRIPTION = "A landscape and text fill a browser page with a raised eye control attached to the title bar."


def draw(s):
    page = browser_window(s, 112, 80)
    preview_page(page, 9, 7, 94, 51)
    control = Surface(s, page.point(83, 61, -3), across=page.across)
    control.plate(rounded(0, 0, 31, 24, 5), 3, EDGE)
    visibility_art(control, 15.5, 12, 10)
