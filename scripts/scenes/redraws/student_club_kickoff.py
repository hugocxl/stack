from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A hanging student banner shows a graduation cap and carries a plus badge on its corner."


def draw(s):
    s.disk(0, 0, 0, 18, 15, 5)
    s.tube([(0, 0, 5), (0, 0, 108)], 2.3)
    s.tube([(-6, 2, 106), (73, 2, 106)], 2.5)
    face = Surface(s, (0, 3, 0))
    ribbon = [(8, 29), (8, 100), (69, 100), (69, 29), (39, 43)]
    face.plate(ribbon, 2)
    face.stroke([(12, 36), (12, 96), (65, 96), (65, 36)])
    for x in (14, 61):
        face.stroke([(x, 100), (x, 105)], EDGE)
    cover_cap(face, 39, 72, 35)
    badge(s, "plus", *face.point(69, 97), 12)
