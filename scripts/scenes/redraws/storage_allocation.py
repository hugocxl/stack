from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import database

DESCRIPTION = "Radial dividers partition the top of a database cylinder, and hatching marks one allocated sector."


def draw(s):
    radius, top = 31, 33
    database(s, 0, 0, radius, pitch=11)
    for angle in (0, 94, 195, 275):
        edge = oval(0, 0, radius, radius, angle, angle, 1)[0]
        s.line([(0, 0, top), (*edge, top)], EDGE)
    for x in (6, 12, 18, 24):
        y = (radius ** 2 - x ** 2) ** .5 - 2
        s.line([(x, 2, top), (x, y, top)], DETAIL)
