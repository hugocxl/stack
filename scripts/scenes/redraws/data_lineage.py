from math import sqrt

from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import database, document_node, level_face

DESCRIPTION = "Two directed branches connect a root database cylinder to its derived data records."


def draw(s):
    bottom, radius = 75, 25
    database(s, bottom, radius, 38)
    p = level_face
    front = radius / sqrt(2)
    s.line([(front, front, bottom), p(0, 45)], EDGE)
    for x in (-48, 48):
        arrow(s, [p(0, 45), p(x, 45), p(x, 29)], EDGE, head=6)
        document_node(s, x - 14, 0, width=28, height=29)
