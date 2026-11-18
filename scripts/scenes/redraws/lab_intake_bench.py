from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w4 import sample_vial

DESCRIPTION = "Two capped, labeled sample vials stand in the fitted wells of a specimen rack."


def draw(s):
    top = 19
    spots = ((20, 19), (50, 19))
    s.box(0, 0, 0, 70, 38, 4, 3)
    for x, y in ((4, 4), (62, 4), (4, 30), (62, 30)):
        s.box(x, y, 4, 4, 4, 13, 1)
    rim = [(x, y, top) for x, y in rounded(0, 0, 70, 38, 4)]
    wells = [[(u, v, top) for u, v in oval(x, y, 11.5, 12)[:-1]] for x, y in spots]
    s.face(rim, openings=wells)
    for x, y in spots:
        sample_vial(s, lambda u, v, h: (x + .707*(u + v), y + .707*(v - u), h + 10))
    s.face([(0, 38, top), (70, 38, top), (70, 38, 14), (0, 38, 14)], EDGE)
    s.face([(70, 0, top), (70, 38, top), (70, 38, 14), (70, 0, 14)], EDGE)
    s.line([(11, 38, 16.5), (26, 38, 16.5)], DETAIL)
