from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "An open laptop displays a browser window with a clock badge over its upper-right corner."


def draw(s):
    display = Surface(s, (0, 9, 4), rise=(-.17, .99), back=(0, -.99, -.17))
    display.plate(rounded(0, 0, 92, 62, 4), 6)
    display.rect(6, 8, 80, 48, 2, EDGE)
    display.rules(6, 44, [80], ink=EDGE)
    display.rect(31, 47, 40, 6, 2)
    for x in (12, 19):
        display.oval(x, 50, 1.3, 1.3, DETAIL)
    display.rules(15, 31, [29, 47], gap=9)

    s.box(0, 3, 0, 92, 54, 5, 4)
    deck = Surface(s, (0, 57, 5), rise=(-1, 0))
    deck.rect(10, 22, 72, 20, 3)
    deck.rules(15, 35, [62, 62], gap=6)
    deck.rect(33, 5, 26, 11, 2)
    badge(s, "clock", *display.point(87, 51, -3), 15)
