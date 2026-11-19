from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import Surface
from scenes.redraws._w5 import clipboard
from scenes.redraws.evening_routine import printed_glyph

DESCRIPTION = "A medical clipboard shows a cross in its header above three scheduled care rows."


def draw(s):
    page = Surface(s, clipboard(s, 69, 91))
    printed_glyph(page, "plus", 21, 65, 13, BOLD)
    page.rows(38, 69, (19, 15), step=-7, ink=EDGE)
    page.line([(10, 53), (59, 53)], DETAIL)
    for z, width in ((42, 29), (29, 25), (16, 31)):
        page.frame(13, z - 4, 10, 8, 1, EDGE)
        page.rows(13, z + 1, (10,), ink=DETAIL)
        for x in (15, 21):
            page.line([(x, z + 2), (x, z + 5)], EDGE)
        page.rows(29, z + 2, (width, width - 8), step=-5, ink=DETAIL)
