from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import database
from scenes.systems_shapes import bezel

DESCRIPTION = "An arrow leads from the newest entry of a standing spiral journal to a database cylinder."


def draw(s):
    s.box(-54, -8, 0, 49, 13, 57, 2)
    bezel(s, -50, 5, 4, 40, 48, DETAIL, 2)
    for x in (-44, -32, -20):
        s.tube([(x, -4, 56), (x, -4, 61), (x, 4, 61), (x, 7, 57), (x, 7, 52)],
               1.4, EDGE)
    for z, width in ((39, 27), (31, 23), (23, 29)):
        s.line([(-45, 5, z), (-45 + width, 5, z)], DETAIL)
    bezel(s, -46, 5, 8, 34, 9, EDGE, 2)
    s.line([(-41, 5, 12.5), (-17, 5, 12.5)], EDGE)
    database(s, 30, -10, 18, pitch=9)
    arrow(s, [(-12, 5, 12.5), (0, 5, 12.5), (9, 1, 12.5)], BOLD, head=5)
