from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge

DESCRIPTION = "A sloped settings console has three faders aligned with their center ticks and an attached check badge."


def draw(s):
    def face(x, z):
        return x, 39 - z, z

    s.face([(0, 6, 0), (75, 6, 0), (75, 6, 33), (0, 6, 33)])
    s.face([(75, 6, 0), face(75, 0), face(75, 33)])
    s.face([face(0, 0), face(75, 0), face(75, 33), face(0, 33)])
    for x in (17, 37, 57):
        s.line([face(x, 5), face(x, 28)], EDGE)
        for offset in (-1, 1):
            s.line([face(x + offset*6.5, 16.5), face(x + offset*9, 16.5)], EDGE)
        knob = rounded(x - 5, 13.9, 10, 5.2, 1.6)
        s.face([(u, y + .4, z + .4) for u, y, z in (face(a, b) for a, b in knob)], EDGE)
    badge(s, "check", *face(73, 27), 12.7)
