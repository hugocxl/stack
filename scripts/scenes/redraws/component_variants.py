from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "Three aligned button variants share a control strip and carry the same right arrow at different sizes."


def draw(s):
    strip = Surface(s, (0, 0, 0), rise=(-.76, .65), back=(0, -.65, -.76),
                    across=(.92, -.39))
    strip.plate(rounded(0, 0, 115, 56, 7), 8)
    for x, w, h, r, depth in ((8, 24, 21, 3, 4), (39, 29, 26, 7, 5), (75, 32, 30, 12, 6)):
        key = Surface(s, strip.point(x, 23 - h / 2, -depth), rise=strip.rise,
                      back=strip.back, across=strip.across)
        key.plate(rounded(0, 0, w, h, r), depth, EDGE)
        printed_glyph(key, "arrow", w / 2, h / 2, w * .30, BOLD)
    strip.rules(9, 46, [24], ink=DETAIL)
    strip.rules(40, 46, [27], ink=DETAIL)
    strip.rules(77, 46, [28], ink=DETAIL)
