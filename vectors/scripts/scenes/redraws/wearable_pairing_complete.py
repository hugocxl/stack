from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._sf import squircle
from scenes.redraws.sleep_tracking import smartwatch

DESCRIPTION = "A smartwatch shows a phone beside a wireless signal and carries a pairing check badge."


def draw(s):
    screen = smartwatch(s)
    phone = [(u - 12, v + 23) for u, v in squircle(12, 21, 3)]
    screen.line(phone + phone[:1], EDGE)
    screen.line([(-8, 26), (-4, 26)], DETAIL)
    glyph(s, "wifi", *screen.at(7, 35), 8, EDGE)
    badge(s, "check", *screen.at(22, 12), 13)
