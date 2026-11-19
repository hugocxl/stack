from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import panel_coin
from scenes.systems_shapes import bezel

DESCRIPTION = "A heart heads a phone donation form with three coin amounts and the middle radio button selected."


def draw(s):
    s.box(-25, -10, 0, 50, 10, 81, 5)
    bezel(s, -21, 0, 6, 42, 66, EDGE, 3)
    s.line([(-6, 0, 76), (6, 0, 76)], DETAIL)
    glyph(s, "heart", 0, 0, 61, 12, EDGE)
    for row, z in enumerate((45, 33, 21)):
        s.line([(x, 0, a) for x, a in oval(-13, z, 3.8, 3.8, count=24)], EDGE)
        if row == 1:
            glyph(s, "dot", -13, 0, z, 7, EDGE)
        for i in range(row + 1):
            panel_coin(s, -2 + i * 8, 0, z, 3.3)
        s.line([(-17, 0, z - 6), (17, 0, z - 6)], DETAIL)
