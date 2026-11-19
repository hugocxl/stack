from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import panel_coin
from scenes.systems_shapes import bezel

DESCRIPTION = "A funding application in an open portfolio has a coin-marked amount field and an upward submission badge."


def draw(s):
    s.face([(-30, -20, 0), (38, -6, 0), (38, -6, 68), (-30, -20, 68)], EDGE)
    s.box(-34, -6, 0, 74, 6, 68, 2)
    s.box(-29, 0, 5, 61, 2.5, 57, 1.4)
    s.line([(-22, 2.5, 54), (9, 2.5, 54)], EDGE)
    for z, length in ((44, 43), (37, 33), (30, 39)):
        s.line([(-22, 2.5, z), (-22 + length, 2.5, z)], DETAIL)
    bezel(s, -23, 2.5, 11, 46, 13, EDGE, 1.5)
    panel_coin(s, -15, 2.5, 17.5, 4.2)
    s.line([(-6, 2.5, 17), (17, 2.5, 17)], EDGE)
    badge(s, "up", 37, 1, 59, 12)
