from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A donation box with a coin slot and heart emblem carries a refresh badge."


def draw(s):
    s.box(0, 0, 0, 76, 48, 56, 5)
    s.box(-2, -2, 52, 80, 52, 8, 3)
    top = Surface(s, (0, 48, 60), rise=(-1, 0), back=(0, 0, -1))
    top.rect(19, 19, 35, 6, 2, EDGE)
    front = Surface(s, (0, 48, 0))
    printed_glyph(front, "heart", 34, 30, 22, BOLD)
    front.rules(25, 11, [18], ink=DETAIL)
    badge(s, "refresh", 75, 49, 51, 15)
