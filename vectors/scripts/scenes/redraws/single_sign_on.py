from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import panel, physical_key

DESCRIPTION = "A single key branches into three app windows."


def draw(s):
    face = lambda x, z: (x, 0, z)
    physical_key(s, lambda x, z: face(6 + x, 31 + z))
    s.line([face(30, 31), face(37, 31), face(44, 52), face(52, 52)], EDGE)
    s.line([face(37, 31), face(52, 31)], EDGE)
    s.line([face(37, 31), face(44, 10), face(52, 10)], EDGE)
    for z in (2, 23, 44):
        panel(s, rounded(52, z, 25, 16, 2), face, 2.3)
        s.line([face(53, z + 11), face(76, z + 11)], DETAIL)
        s.line([face(56, z + 13.5), face(58, z + 13.5)], EDGE)
