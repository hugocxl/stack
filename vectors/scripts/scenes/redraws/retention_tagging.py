from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.systems_shapes import bezel

DESCRIPTION = "A punched label shows a large clock beside a short duration field."


def draw(s):
    body = [(-36, 0), (25, 0), (42, 18), (25, 36), (-36, 36)]
    hole = oval(30, 18, 3.7, 3.7, count=24)
    s.face([(x, -5, z) for x, z in body], EDGE)
    for a, b in zip(body, body[1:] + body[:1]):
        if b[1] - a[1] > b[0] - a[0]:
            s.face([(a[0], -5, a[1]), (b[0], -5, b[1]), (b[0], 0, b[1]), (a[0], 0, a[1])], EDGE)
    s.face([(x, 0, z) for x, z in body], EDGE, openings=[[(x, 0, z) for x, z in hole]])

    s.line([(x, 0, z) for x, z in oval(-20, 18, 10, 10, count=40)], EDGE)
    glyph(s, "clock", -20, 0, 18, 10)
    bezel(s, -3, 0, 13, 23, 10, EDGE, 2)
    s.line([(2, 0, 18), (14, 0, 18)], DETAIL)
