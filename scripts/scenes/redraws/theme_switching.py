from math import cos, radians, sin

from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import browser_window, printed_glyph

DESCRIPTION = "A split browser pairs a sun with a crescent moon, and a circular switch arrow bridges the two themes."


def draw(s):
    page = browser_window(s, 114, 80)
    page.stroke([(57, 0), (57, 65)], EDGE)
    page.oval(28, 42, 8, 8, EDGE)
    for degrees in range(0, 360, 45):
        angle = radians(degrees)
        page.stroke([(28 + r * cos(angle), 42 + r * sin(angle)) for r in (12, 16)], EDGE)
    printed_glyph(page, "moon", 86, 42, 21)
    for x in (13, 71):
        page.rules(x, 16, [30, 21], gap=6)
    badge(s, "refresh", *page.point(57, 36, -4), 13)
