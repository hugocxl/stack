from geometry import EDGE
from scenes.redraws._w4 import open_book, printed_glyph

DESCRIPTION = "An open sleep journal has an embossed crescent on its inside cover and ruled entries on the facing page."


def draw(s):
    cover, entries = open_book(s)
    cover.frame(10, 10, 43, 53, 3)
    printed_glyph(cover, "moon", 31, 36, 24, EDGE, down=True)
    entries.rows(76, 20, (23,), ink=EDGE)
    entries.rows(76, 30, (34, 25, 31, 27), step=8)
