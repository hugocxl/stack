from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import carrier_plane, carrier_van, price_tag

DESCRIPTION = "A carrier comparison card pairs two shipping services with price tags showing different coin amounts."


def draw(s):
    s.box(-45, -9, 0, 90, 9, 54, 3)
    s.line([(-39, 0, 27), (39, 0, 27)], DETAIL)
    carrier_van(s, -37, 0, 27, 35)

    carrier_plane(s, -36, 0, 5, 32)

    for bottom, count in ((33, 1), (6, 3)):
        price_tag(s, 10, 1, bottom, 29)
        for index in range(count):
            x = 26 + (index - (count - 1) / 2) * 4
            points = oval(x, bottom + 8, 3.5, 4.7, count=24)[:-1]
            s.face([(a, 1, b) for a, b in points], EDGE)
