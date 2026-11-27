from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import BACK, left_face, lip, plate, squircle, turned

DESCRIPTION = "A hard hat rests in front of a standing phone that carries a return-call badge."


def draw(s):
    face = left_face(-24, 0, 0)
    plate(s, face, squircle(48, 92, 10), 6, (0, -1, 0))
    inner = [face(u + 4, v + 4) for u, v in squircle(40, 84, 7)]
    s.line(inner + inner[:1], DETAIL)
    turned(s, [(26, 0), (26, 2.4), (16, 3.4), (17, 13), (14, 20), (8, 24), (.4, 25)], 34, 30, 0, steps=4)
    lip(s, 34, 30, 3.6, 16.5, EDGE, -60, 150)
    s.line([(34 - 11.7, 30 + 11.7, 3.6), (34 - 9, 30 + 9, 16), (34 - 4, 30 + 4, 23.5)], DETAIL)
    badge(s, "back", *face(48, 84), 12)
