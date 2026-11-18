from geometry import EDGE
from scenes.redraws._w1 import database

DESCRIPTION = "A dashed three-dimensional enclosure surrounds a single database cylinder."


def draw(s):
    corners = [(-32, -32), (32, -32), (32, 32), (-32, 32)]
    for z in (0, 47):
        s.line([(*corner, z) for corner in corners + corners[:1]], EDGE, dashed=True)
    for x, y in corners:
        s.line([(x, y, 0), (x, y, 47)], EDGE, dashed=True)
    database(s, 0, 0, 23, bottom=2, pitch=12)
