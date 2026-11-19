from geometry import DETAIL, EDGE
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w5 import folded_sheet, rect

DESCRIPTION = "A folded-corner data sheet shows a table beneath an outward arrow and carries a clock badge at its lower corner."


def draw(s):
    face = folded_sheet(s, w=61, h=62, lean=.64)
    rect(s, face, 9, 10, 43, 31, .7, EDGE)
    for z in (20, 30):
        s.line([face(9, z), face(52, z)], DETAIL)
    for x in (23, 35):
        s.line([face(x, 10), face(x, 41)], EDGE)
    for stroke in _strokes("arrow", 9):
        s.line([face(25 + x, 51 + z) for x, z in stroke], EDGE)
    badge(s, "clock", *face(61, 12), 13)
