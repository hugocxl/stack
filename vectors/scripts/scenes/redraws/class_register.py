from geometry import EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import Surface

DESCRIPTION = "A standing attendance register has a column of checks beside its student rows."


def draw(s):
    cover = Surface(s, (0, 0, 0))
    cover.plate(rounded(0, 0, 83, 95, 4), 13)
    cover.plate(rounded(6, 5, 71, 85, 2), 2)
    cover.rules(19, 79, [43], ink=EDGE)
    cover.rect(20, 15, 48, 55, 1)
    cover.stroke([(55, 15), (55, 70)], EDGE)
    for row, v in enumerate((63, 49, 35, 22)):
        cover.rules(26, v + 1, [18 + (row % 2) * 4], ink=EDGE)
        if row != 3:
            glyph(s, "check", 61.5, 0, v, 5)
            cover.rules(20, v - 7, [48])
    cover.rect(58.4, 19, 6.2, 6.2, 1, EDGE)
    for v in (28, 66):
        s.tube([(-2, -4, v), (-2, .5, v), (4, 3.4, v), (11, 1, v)], 1.6)
