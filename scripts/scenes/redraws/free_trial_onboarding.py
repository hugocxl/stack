from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import front_surface, printed_glyph, upright

DESCRIPTION = "A phone welcome screen shows a three-step progress track with its first step highlighted."


def draw(s):
    angle = 12
    upright(s, rounded(0, 0, 60, 96, 8), 8, 10, angle=angle)
    phone = front_surface(s, angle=angle, y=8)
    phone.frame(5, 6, 50, 84, 5, DETAIL)
    phone.rows(24, 84, (12,), ink=EDGE)
    phone.frame(15, 43, 30, 22, 4, EDGE)
    printed_glyph(phone, "play", 29, 54, 13, EDGE)
    phone.rows(16, 35, (28, 19), step=-6)
    for a, b in ((22.3, 27.6), (34.4, 39.6)):
        phone.line([(a, 18), (b, 18)], DETAIL)
    for x in (31, 43):
        phone.oval(x, 18, 3.4, 3.4, EDGE)
    phone.oval(18, 18, 4.3, 4.3, BOLD)
    phone.oval(18, 18, 1.3, 1.3, EDGE)
