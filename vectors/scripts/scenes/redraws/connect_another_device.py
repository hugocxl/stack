from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import left_face, plate, squircle
from scenes.redraws._w2 import laptop

DESCRIPTION = "A phone stands beside an open laptop, a plus badge between them."


def draw(s):
    laptop(s, 96, 58)
    phone = left_face(-44, 18, 0)
    plate(s, phone, squircle(30, 58, 7), 5, (0, -1, 0))
    inner = [phone(u + 3, v + 5) for u, v in squircle(24, 48, 4)]
    s.line(inner + inner[:1], DETAIL)
    badge(s, "plus", -6, 18, 30, 11)
