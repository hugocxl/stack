from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, warning
from scenes.redraws._w5 import clipboard

DESCRIPTION = "An incident statement on a clipboard shows a compact warning heading and a check badge."


def draw(s):
    face = clipboard(s, 60, 67)
    warning(s, 18, -16, 40, 17)
    s.line([face(30, 48), face(49, 48)], EDGE)
    s.line([face(30, 42), face(45, 42)], DETAIL)
    for z, length in ((31, 38), (24, 42), (17, 29)):
        s.line([face(9, z), face(9 + length, z)], DETAIL)
    badge(s, "check", *face(56, 20), 12)
