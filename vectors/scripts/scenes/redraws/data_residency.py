from geometry import EDGE
from scenes.redraws._w2 import database

DESCRIPTION = "An irregular geographic boundary encloses a three-tier database cylinder."


def draw(s):
    boundary = [(-45, -23), (-37, -42), (33, -42), (40, -33),
                (38, -24), (45, -18), (47, -6), (40, 4), (42, 17),
                (47, 26), (46, 35), (39, 37), (33, 27), (22, 24),
                (13, 32), (-3, 30), (-15, 39), (-30, 40), (-32, 26),
                (-44, 16), (-41, 7), (-49, -5), (-45, -23)]
    s.line([(x, y, 0) for x, y in boundary], EDGE)
    database(s, 0, 25, 45)
