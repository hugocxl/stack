from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w5 import rect

DESCRIPTION = "A bordered erasure certificate shows a crossed-out hard drive and a check badge at its lower corner."


def draw(s):
    s.box(-5, -73, 0, 5, 73, 54, 1)
    face = lambda x, z: (0, -x, z)
    rect(s, face, 5, 5, 63, 44, 1.5, DETAIL)
    rect(s, face, 12, 26, 31, 18, 2.6)
    s.line([face(x, z) for x, z in oval(23, 35, 6, 6, count=28)], EDGE)
    s.line([face(23, 35), face(28, 32), face(37, 32)], DETAIL)
    for stroke in _strokes("slash", 18):
        s.line([face(28 + x, 35 + z) for x, z in stroke], BOLD)
    for z, length in ((19, 39), (12, 31)):
        s.line([face(12, z), face(12 + length, z)], DETAIL)
    badge(s, "check", *face(67, 10), 12)
