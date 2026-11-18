from geometry import EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws.sleep_tracking import smartwatch

DESCRIPTION = "A smartwatch shows a phone with a wireless signal and carries a pairing check badge."


def draw(s):
    screen = smartwatch(s)
    screen.frame(-12, 24, 13, 20, 2.5, EDGE)
    screen.rows(-8, 27, (5,))
    glyph(s, "wifi", *screen.at(7, 37), 7, EDGE)
    badge(s, "check", *screen.at(22, 15), 13)
