from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import price_tag

DESCRIPTION = "A ribbon-wrapped gift box carries a tag marked with a crossed-out coin."


def draw(s):
    s.box(-32, -26, 0, 64, 52, 34, 2.5)
    s.box(-34, -28, 31, 68, 56, 8, 2)
    for x in (-5, 5):
        s.line([(x, -27, 39), (x, 28, 39), (x, 28, 31)], EDGE)
        s.line([(x, 26, 31), (x, 26, 0)], DETAIL)
    for y in (-5, 5):
        s.line([(-33, y, 39), (34, y, 39), (34, y, 31)], EDGE)
        s.line([(32, y, 31), (32, y, 0)], DETAIL)

    for sign in (-1, 1):
        s.face([(0, 0, 41), (sign * 11, -6, 52), (sign * 20, -3, 52),
                (sign * 19, 4, 47), (sign * 10, 6, 42)], EDGE)
        s.line([(sign * 3, 2, 40), (sign * 11, 14, 41), (sign * 16, 16, 39)], EDGE)
    s.box(-3, -3, 39, 6, 6, 5, 1.2)

    anchor = (9, 28, 36)
    eye = price_tag(s, 15, 33, 6, 31)
    s.line([anchor, (19, 34, 29), eye], EDGE)
    s.line([(a, 33, b) for a, b in oval(35, 14.9, 5.7, 5.7, count=27)], EDGE)
    glyph(s, "slash", 35, 33, 14.9, 8.8)
