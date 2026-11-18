from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A community center with a columned entrance carries a clock badge at its roof edge."


def civic_emblem(s, x, y, z, size):
    def stroke(points):
        s.line([(x + u * size, y, z + v * size) for u, v in points], EDGE)

    stroke([(-1, .25), (0, .85), (1, .25), (-1, .25)])
    for u in (-.67, 0, .67):
        stroke([(u, .25), (u, -.55)])
    stroke([(-1, -.55), (1, -.55)])


def draw(s):
    s.box(-37, -23, 0, 74, 50, 5, 1.5)
    s.box(-35, -22, 5, 70, 40, 38, 1.3)
    s.box(-38, -24, 43, 76, 44, 5, 1.3)
    for x in (-30, 17):
        bezel(s, x, 18, 16, 13, 15, DETAIL, 1)
    bezel(s, -12, 18, 6, 24, 24, EDGE, 1)
    s.line([(0, 18, 6), (0, 18, 30)], DETAIL)
    for x in (-16, 16):
        s.disk(x, 24, 5, 2.1, 2.1, 30)
    s.box(-20, 17, 34, 40, 12, 5, 1.3)
    s.face([(-21, 29, 39), (21, 29, 39), (0, 29, 50)], EDGE)
    badge(s, "clock", 37, 1, 43, 12)
