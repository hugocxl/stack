from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w5 import folded_sheet

DESCRIPTION = "A standing incident notice carries a warning triangle beside its headline."


def draw(s):
    face = folded_sheet(s, 68, 62, lean=.25, fold=12)
    for z, length in ((51, 27), (43, 22)):
        s.line([face(31, z), face(31 + length, z)], EDGE)
    s.line([face(7, 34), face(61, 34)], DETAIL)
    for z, length in ((26, 48), (19, 45), (12, 31)):
        s.line([face(9, z), face(9 + length, z)], DETAIL)
    warning(s, 13, -8, 37, 24)
