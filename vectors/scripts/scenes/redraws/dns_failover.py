from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import web_globe
from scenes.systems_shapes import bezel

DESCRIPTION = "A globe labels a two-row DNS record card, and a bent arrow routes from its primary row to its backup row."


def draw(s):
    s.box(-42, -13, 0, 84, 13, 55, 4)
    web_globe(s, -29, 0, 43, 5)
    s.line([(-18, 0, 43), (11, 0, 43)], DETAIL)

    for z, width in ((26, 25), (10, 21)):
        bezel(s, -34, 0, z - 4, 53, 10, EDGE, 2)
        s.line([(x, 0, y) for x, y in oval(-27, z + 1, 1.7, 1.7, count=14)], EDGE)
        for x in (-21, -9, 2):
            s.line([(x, 0, z + 1), (x + width / 5, 0, z + 1)], EDGE)

    points = [(19, 0, 27), (26, 0, 27), (30, 0, 25), (32, 0, 21),
              (32, 0, 17), (30, 0, 13), (28, 0, 11), (22, 0, 11)]
    arrow(s, points, BOLD, head=6)
