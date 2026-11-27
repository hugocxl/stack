from scenes.redraws._kit import badge
from scenes.redraws._sf import bolt, left_face, plate, squircle

DESCRIPTION = "An upright backup battery with a lightning mark carries a return badge."


def draw(s):
    s.box(-10, -12, 74, 20, 12, 6, 2)
    face = left_face(-30, 0, 0)
    plate(s, face, squircle(60, 76, 10), 24, (0, -1, 0))
    bolt(s, lambda u, v: face(30 + u, 38 + v), 14)
    badge(s, "back", 30, 0, 8, 13)
