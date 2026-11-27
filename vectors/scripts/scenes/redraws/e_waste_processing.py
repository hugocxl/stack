from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import left_face, plate, squircle

DESCRIPTION = "A discarded phone leans out of an open collection bin that carries a refresh badge."


def draw(s):
    W, D, H = 72, 46, 32
    s.face([(0, 0, 0), (W, 0, 0), (W, 0, H), (0, 0, H)], EDGE)
    s.face([(0, 0, 0), (0, D, 0), (0, D, H), (0, 0, H)], EDGE)
    phone = lambda u, v: (22 + u, 20 - v*.3, 8 + v*.95)
    plate(s, phone, squircle(28, 54, 7), 4, (0, -1, 0))
    inner = [phone(u + 3, v + 5) for u, v in squircle(22, 44, 4)]
    s.line(inner + inner[:1], DETAIL)
    s.face([(W, 0, 0), (W, D, 0), (W, D, H), (W, 0, H)], EDGE)
    s.face([(0, D, 0), (W, D, 0), (W, D, H), (0, D, H)], EDGE)
    s.line([(8, D, H - 8), (W - 8, D, H - 8)], DETAIL)
    badge(s, "refresh", W - 4, D, 14, 12)
