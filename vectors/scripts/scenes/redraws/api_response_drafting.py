from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import left_face, plate, smooth, squircle

DESCRIPTION = "A standing response card is printed with curly braces around three key and value rows."


def draw(s):
    w, h = 92, 70
    face = left_face(-w/2, 0, 0)
    plate(s, face, squircle(w, h, 7), 6, (0, -1, 0))
    brace = smooth([(16, 60), (11, 59), (10, 50), (10, 40), (6, 35), (10, 30), (10, 20), (11, 11), (16, 10)], 4)
    s.line([face(u, v) for u, v in brace], BOLD)
    s.line([face(w - u, v) for u, v in brace], BOLD)
    for v, a, b in ((48, 14, 22), (35, 18, 16), (22, 12, 26)):
        s.line([face(24, v), face(24 + a, v)], EDGE)
        s.line([face(26 + a, v + 2), face(26 + a, v + 2.4)], EDGE)
        s.line([face(26 + a, v - 2), face(26 + a, v - 1.6)], EDGE)
        s.line([face(32 + a, v), face(32 + a + b, v)], DETAIL)
