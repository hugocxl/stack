from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A member pass sticks out of an open envelope with an outward arrow badge on its corner."


def draw(s):
    back = Surface(s, (0, -11, 3))
    back.plate([(0, 0), (95, 0), (95, 43), (52, 72), (43, 72), (0, 43)], 3)
    card = Surface(s, (15, -8, 25), rise=(-.1, 1))
    card.plate(rounded(0, 0, 64, 47, 4), 4)
    card.oval(17, 30, 10, 10)
    printed_glyph(card, "star", 17, 30, 7)
    card.rules(34, 34, [22, 16], gap=8)
    s.face([(95, -11, 0), (95, 0, 0), (95, 0, 43), (95, -11, 43)])
    front = Surface(s, (0, 0, 0))
    front.plate([(0, 0), (95, 0), (95, 44), (48, 21), (0, 44)], 5)
    front.stroke([(0, 1), (34, 26)], EDGE)
    front.stroke([(94, 1), (61, 27)], EDGE)
    badge(s, "arrow", 95, 2, 44, 16)
