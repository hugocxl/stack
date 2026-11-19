from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, clipboard, strike_through

DESCRIPTION = "A document on a clipboard shows an active insertion caret beside a crossed-out Wi-Fi badge."


def draw(s):
    page = clipboard(s, 77, 84)
    page.rules(15, 58, [38], ink=EDGE)
    page.rules(15, 44, [45, 41, 26], gap=10)
    page.stroke([(44, 20), (44, 32)], BOLD)
    page.rules(41, 20, [6], ink=BOLD)
    page.rules(41, 32, [6], ink=BOLD)
    x, y, z = page.point(74, 67, -5)
    badge(s, "wifi", x, y, z, 17)
    strike_through(Surface(s, (x, y, z)), 0, 0, 13)
