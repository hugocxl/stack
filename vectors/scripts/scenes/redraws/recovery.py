from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import folded_sheet, rect

DESCRIPTION = "A saved-state file shows a disk pictogram and carries a prominent circular return-arrow badge."


def draw(s):
    face = folded_sheet(s, 55, 63)
    outline = [(10, 16), (39, 16), (39, 42), (35, 46), (10, 46), (10, 16)]
    s.line([face(x, z) for x, z in outline], EDGE)
    rect(s, face, 16, 36, 15, 10, 1.3, EDGE)
    s.line([face(26, 39), face(26, 44)], DETAIL)
    rect(s, face, 15, 16, 19, 13, 1.3, DETAIL)
    badge(s, "refresh", *face(51, 11), 14)
