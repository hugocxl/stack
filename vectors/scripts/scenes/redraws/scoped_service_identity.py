from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import key_mark, panel, rect

DESCRIPTION = "A service credential shows a terminal prompt and one bracketed permission beside an engraved key."


def draw(s):
    face = lambda x, z: (x, -z * .48, z)
    panel(s, rounded(0, 0, 69, 43, 5), face, 7)
    rect(s, face, 7, 24, 20, 12, 2.5, EDGE)
    s.line([face(11, 33), face(15, 30), face(11, 27)], EDGE)
    s.line([face(18, 27), face(23, 27)], EDGE)
    s.line([face(34, 32), face(58, 32)], DETAIL)
    s.line([face(7, 19), face(62, 19)], DETAIL)
    s.line([face(x, z) for x, z in [(11, 14), (7, 14), (7, 6), (11, 6)]], EDGE)
    s.line([face(x, z) for x, z in [(37, 14), (41, 14), (41, 6), (37, 6)]], EDGE)
    s.line([face(14, 10), face(34, 10)], EDGE)
    key_mark(s, face, 49, 10, .59)
