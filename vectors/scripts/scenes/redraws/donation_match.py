from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import money_coin, rect

DESCRIPTION = "Two matching currency coins line up over the single slot of a heart-marked donation box."


def draw(s):
    s.box(0, 0, 0, 71, 42, 36, 4)
    top = lambda x, y: (x, y, 36)
    rect(s, top, 8, 15, 55, 7, 2, EDGE)
    for x in (22, 49):
        money_coin(s, x, 19, 50, 13)
    front = lambda x, z: (x, 42, z)
    glyph(s, "heart", *front(36, 17), 15, EDGE)
    s.line([(4, 42, 31), (67, 42, 31)], DETAIL)
