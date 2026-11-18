from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import outline

DESCRIPTION = "An instrument shows a partially used error allowance as a hatched bar inside a closed track."


def draw(s):
    s.box(0, -23, 0, 116, 23, 55, 6)
    glyph(s, "exclaim", 18, 0, 29, 13, EDGE)
    s.line([(30, 0, 14), (30, 0, 43)], DETAIL)
    outline(s, 40, 0, 22, 65, 17, 3, EDGE)
    s.line([(42, 0, 23), (79, 0, 23), (79, 0, 38), (42, 0, 38)], BOLD)
    for x in (43, 51, 59, 67):
        s.line([(x, 0, 24), (x + 7, 0, 37)], DETAIL)
    for x, length in ((42, 5), (57, 3), (73, 3), (88, 3), (103, 5)):
        s.line([(x, 0, 16), (x, 0, 16 - length)], DETAIL)
