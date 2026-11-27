from geometry import DETAIL, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "A pair of over-ear headphones frames a play badge between its earcups."


def draw(s):
    angle = -25
    face = front_surface(s, angle=angle)
    band = [face.at(u, z) for u, z in oval(0, 43, 39, 41, 0, 180, 48)]
    s.tube(band, 4.5)
    face.line(oval(0, 42, 35, 37, 14, 166, 40), DETAIL)
    for u in (-38, 38):
        s.tube([face.at(u, 47), face.at(u, 37), face.at(u, 34)], 3.4)
        upright(s, rounded(u - 9, 1, 18, 38, 5), 4, 14, angle=angle)
        cushion = front_surface(s, angle=angle, y=4)
        for x in (u - 4, u + 4):
            cushion.line([(x, 8), (x, 31)], DETAIL)
    badge(s, "play", *face.at(21, 26), 13)
