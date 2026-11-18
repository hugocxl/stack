from geometry import BOLD, DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A magnifier frames the two forwarding sockets on the face of a proxy server."


def draw(s):
    s.box(-43, -38, 0, 86, 38, 45, 4)
    bezel(s, -34, 0, 13, 20, 16, DETAIL, 2)
    for x in (-30, -24, -18):
        s.line([(x, 0, 21), (x + 2, 0, 21)], EDGE)
    for x in (2, 21):
        bezel(s, x - 6, 0, 19, 12, 13, EDGE, 1)
        s.line([(x - 2, 0, 29), (x + 2, 0, 29)], DETAIL)

    s.tube([(27, 4, 10), (45, 4, -8)], 3.2, EDGE)
    for radius, ink in ((21, BOLD), (17.5, DETAIL)):
        s.line([(x, 4, z) for x, z in oval(13, 25, radius, radius)], ink)
