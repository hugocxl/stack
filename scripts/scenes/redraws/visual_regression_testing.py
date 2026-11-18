from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import browser_header
from scenes.systems_shapes import bezel

DESCRIPTION = "Two browser screenshots show the same layout, with a dashed outline around the changed button."


def screenshot(s, x, y, changed):
    s.box(x, y - 6, 0, 60, 6, 48, 3)
    browser_header(s, x + 5, y, 42, 50)
    bezel(s, x + 8, y, 21, 44, 10, DETAIL, 2)
    s.line([(x + 13, y, 26), (x + 38, y, 26)], DETAIL)
    button_width = 27 if changed else 12
    bezel(s, x + 10, y, 8, button_width, 7, EDGE, 2)
    if changed:
        corners = [(x + 6, 5), (x + 40, 5), (x + 40, 18), (x + 6, 18)]
        s.line([(a, y, b) for a, b in corners + corners[:1]], BOLD, dashed=True)


def draw(s):
    screenshot(s, -48, 11, False)
    screenshot(s, 9, -1, True)
