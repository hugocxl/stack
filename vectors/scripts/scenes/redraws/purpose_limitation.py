from geometry import DETAIL, EDGE
from scenes.redraws._kit import _strokes
from scenes.redraws._w5 import clipboard, rect

DESCRIPTION = "A data-use clipboard lists three purposes and has a check mark in just one purpose box."


def draw(s):
    face = clipboard(s, 59, 66)
    s.line([face(11, 48), face(36, 48)], DETAIL)
    for z, width in ((14, 23), (26, 28), (38, 19)):
        rect(s, face, 11, z - 3.5, 7, 7, .8, EDGE)
        s.line([face(24, z), face(24 + width, z)], DETAIL)
    for stroke in _strokes("check", 6):
        s.line([face(15.3 + x, 27.3 + z) for x, z in stroke], EDGE)
