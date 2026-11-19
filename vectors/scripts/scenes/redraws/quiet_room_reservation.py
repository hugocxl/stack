from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A room door has a crescent plaque and carries a clock badge for a reservation."


def draw(s):
    upright(s, rounded(0, 0, 68, 112, 2), 15, 15)
    front = Surface(s, lambda u, v: (u, 15, v))
    front.frame(6, 3, 56, 102, 1, EDGE)
    front.line([(11, 8), (11, 99), (57, 99)], DETAIL)
    front.frame(20, 56, 28, 29, 3, DETAIL)
    glyph(s, "moon", 34, 15, 71, 14, EDGE)
    s.box(47, 15, 38, 4, 3, 11, 1)
    s.tube([(49, 19, 44), (39, 19, 44)], 1.3, EDGE)
    badge(s, "clock", 70, 12, 77, 17)
