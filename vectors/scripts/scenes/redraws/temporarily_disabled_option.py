from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge

DESCRIPTION = "A rocker switch on a rounded housing has a slash badge at one corner."


def draw(s):
    s.box(0, 0, 0, 63, 59, 10, 7)
    opening = rounded(12, 8, 39, 43, 4)
    s.line([(x, y, 10) for x, y in [*opening, opening[0]]], DETAIL)
    a, b = (16, 11, 11), (47, 11, 11)
    c, d = (47, 28, 19), (16, 28, 19)
    e, f = (47, 47, 11), (16, 47, 11)
    s.face([b, c, e], DETAIL)
    s.face([a, b, c, d], EDGE)
    s.face([d, c, e, f], EDGE)
    s.line([(25, 17, 14), (38, 17, 14)], DETAIL)
    badge(s, "slash", 63, 5, 16, 14)
