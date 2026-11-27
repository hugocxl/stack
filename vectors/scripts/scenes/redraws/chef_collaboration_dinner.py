from geometry import DETAIL, EDGE
from scenes.redraws._sf import left_face, lip, plate, squircle, turned

DESCRIPTION = "A dinner plate set with a fork and knife sits in front of a standing menu card."


def draw(s):
    card = left_face(-30, -40, 0)
    plate(s, card, squircle(48, 66, 4), 3, (0, -1, 0))
    for v in (50, 42, 34, 26):
        s.line([card(10, v), card(38, v)], DETAIL)
    turned(s, [(30, 0), (32, 3), (33, 4)], 0, 10, 0, steps=2)
    lip(s, 0, 10, 4, 20, DETAIL, -180, 180)
    for dx in (-44, 44):
        s.box(dx - 2, -6, 0, 4, 34, 1.6, 1.5)
