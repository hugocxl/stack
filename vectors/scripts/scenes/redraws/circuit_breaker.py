from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import bolt, left_face, plate, squircle

DESCRIPTION = "A breaker box with a lightning mark has its toggle lever thrown down to the off position."


def draw(s):
    face = left_face(-36, 0, 0)
    plate(s, face, squircle(72, 90, 10), 20, (0, -1, 0))
    slot = [face(26 + u, 30 + v) for u, v in squircle(20, 34, 6)]
    s.line(slot + slot[:1], EDGE)
    bolt(s, lambda u, v: face(36 + u, 76 + v), 7)
    s.tube([face(36, 40), (face(36, 32)[0], 18, face(36, 32)[2])], 3.4, EDGE)
    s.line([face(12, 12), face(60, 12)], DETAIL)
