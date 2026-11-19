from geometry import DETAIL, EDGE
from scenes.redraws._w5 import avatar_mark
from scenes.redraws.hotel_search import magnifier

DESCRIPTION = "An indexed group directory shows three member entries with a magnifier centered on the middle entry."


def draw(s):
    s.box(0, -13, 0, 59, 13, 68, 2)
    for z in (9, 26, 43):
        s.box(57, -8, z, 7, 5, 11, 1)
    face = lambda x, z: (x, 0, z)
    s.line([face(6.5, 3), face(6.5, 65)], EDGE)
    for z, width in ((12.5, 24), (34, 22), (55, 25)):
        avatar_mark(s, face, 18, z, .86)
        s.line([face(31, z + 2), face(31 + width, z + 2)], EDGE)
        s.line([face(31, z - 4), face(42, z - 4)], DETAIL)
    for z in (24, 44):
        s.line([face(9.5, z), face(55, z)], DETAIL)
    magnifier(s, 22, 1, 34, 11.8)
