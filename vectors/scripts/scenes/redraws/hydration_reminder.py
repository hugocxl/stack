from geometry import EDGE, DETAIL, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface

DESCRIPTION = "A reusable water bottle with a carry loop and a droplet emblem carries a clock badge."


def draw(s):
    body = oval(0, 0, 23, 23)[:-1]
    neck = oval(0, 0, 13, 13)[:-1]
    s.disk(0, 0, 0, 23, 23, 69)
    s.solid(body, 69, 13, top=neck, crease=False)
    s.disk(0, 0, 82, 14, 14, 12)
    s.tube([(-9, 1, 92), (-11, 1, 103), (-7, 1, 109),
            (4, 1, 109), (9, 1, 104), (9, 1, 93)], 2.6, EDGE)
    s.ellipse(0, 0, 11, 23, 23, DETAIL, 8, 83)
    face = Surface(s, lambda u, v: (18*.707 + u*.707, 18*.707 - u*.707, v))
    face.outline([(0, 55), *oval(0, 37, 9, 9, 150, 390, 35)], EDGE)
    badge(s, "clock", 26, -2, 67, 16)
