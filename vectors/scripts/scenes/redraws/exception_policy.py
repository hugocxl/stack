from geometry import DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import policy_book, rect

DESCRIPTION = "A policy binder has an outlined exception clause with an arrow that branches outward from the row."


def draw(s):
    face = policy_book(s)
    for z, length in ((40, 31), (31, 27), (13, 23)):
        s.line([face(16, z), face(16 + length, z)], DETAIL)
    rect(s, face, 13, 19, 37, 7, 1.1, EDGE)
    s.line([face(17, 22.5), face(39, 22.5)], EDGE)
    arrow(s, [face(50, 22.5), face(59, 22.5), (67, -4, 31), (78, -10, 32)], head=7)
