from geometry import DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A test flask sits in front of a browser window."


def draw(s):
    s.box(-43, -12, 0, 86, 12, 48, 4)
    s.line([(-40, 0, 33), (40, 0, 33)], EDGE)
    for x in (-35, -29):
        s.line([(x, 0, 40), (x + 1.1, 0, 40)], EDGE)
    bezel(s, -21, 0, 36, 55, 9, EDGE, 4.5)
    bezel(s, -35, 0, 9, 32, 17, DETAIL, 2)
    for z, w in ((23, 16), (16, 21)):
        s.line([(4, 0, z), (4 + w, 0, z)], DETAIL)

    x, y = 37, 10
    s.solid(oval(x, y, 17, 17)[:-1], 0, 33, top=oval(x, y, 5.5, 5.5)[:-1], crease=False)
    s.disk(x, y, 33, 5.5, 5.5, 10)
    s.ring(x, y, 42, 7, 7, 3, wall=2.2)
    s.ellipse(x, y, 10, 13.4, 13.4, EDGE, start=0, end=180)
