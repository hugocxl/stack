from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import price_tag
from scenes.systems_shapes import bezel

DESCRIPTION = "A lidded returnable shipping tote carries a deposit tag marked with stacked coins."


def draw(s):
    s.box(-34, -25, 0, 68, 50, 35, 4)
    s.box(-36, -27, 32, 72, 54, 8, 3)
    for x in (-26, 25):
        s.box(x - 3, 22, 27, 6, 6, 13, 1.2)
    bezel(s, -23, 25, 20, 34, 6, EDGE, 2)
    for x in (-27, -16, -5, 6, 17, 28):
        s.line([(x, 25, 5), (x, 25, 15)], DETAIL)
    for y in (-18, -9, 0, 9, 18):
        s.line([(34, y, 5), (34, y, 25)], DETAIL)

    eye = price_tag(s, 17, 30, 1, 32)
    s.line([(26, 29, 31), (23, 32, 24), eye], EDGE)
    for z in (7.5, 11, 14.5):
        s.line([(a, 30, b) for a, b in oval(36, z, 6.5, 2.6, 180, 360, count=18)], EDGE)
    s.line([(a, 30, b) for a, b in oval(36, 14.5, 6.5, 2.6, 0, 180, count=18)], EDGE)
