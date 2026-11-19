from geometry import DETAIL, EDGE
from scenes.redraws._w5 import avatar_mark, rect, redaction

DESCRIPTION = "A phone displays a profile with a dark masking bar over one field."


def draw(s):
    s.box(0, 0, 0, 7, 47, 72, 3)
    face = lambda u, z: (7, 47 - u, z)
    rect(s, face, 3, 5, 41, 61, 4, EDGE)
    s.line([face(19, 69), face(28, 69)], DETAIL)
    avatar_mark(s, face, 23.5, 48, 1.5)
    s.line([face(12, 29), face(35, 29)], DETAIL)
    rect(s, face, 9, 12, 29, 11, 1.5, DETAIL)
    redaction(s, face, 13, 15.3, 21, 4.4)
