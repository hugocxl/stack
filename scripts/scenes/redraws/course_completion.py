from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A framed course certificate carries a ribbon seal with a large check badge."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 106, 73, 3), 7)
    face.rect(5, 5, 96, 63, 1, EDGE)
    face.rect(9, 9, 88, 55, 1)
    face.rules(24, 53, [58], ink=EDGE)
    face.rules(26, 39, [45, 34, 41], gap=8)
    ribbon = Surface(s, (0, 2, 0))
    ribbon.plate([(78, 16), (80, -9), (87, -4), (93, -12), (95, 17)], 2)
    badge(s, "check", 86, 4, 25, 14)
