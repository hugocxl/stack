from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A timeline card shows three dated event nodes and a lock badge on its upper edge."


def draw(s):
    face = lambda u, h: (u - h * .5, -u * .72, h)
    panel(s, rounded(0, 0, 78, 50, 3), face, 4)
    s.line([face(8, 23), face(70, 23)], EDGE)
    for x, length in ((17, 13), (39, 10), (61, 13)):
        s.face([face(u, v) for u, v in oval(x, 23, 3.8, 3.8, count=24)[:-1]])
        s.line([face(x, 27), face(x, 31)], DETAIL)
        rect(s, face, x - 4.6, 31, 9.2, 9, 1, DETAIL)
        s.line([face(x - 4.5, 37), face(x + 4.5, 37)], DETAIL)
        s.line([face(x - 2, 39), face(x - 2, 42)], EDGE)
        s.line([face(x + 2, 39), face(x + 2, 42)], EDGE)
        s.line([face(x - 6, 13), face(x - 6 + length, 13)], DETAIL)
    badge(s, "lock", *face(76, 48), 13)
