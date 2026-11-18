from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import device, rect

DESCRIPTION = "An upright smartphone displays a device identifier with a check badge at its lower corner."


def draw(s):
    face = device(s)
    rect(s, face, 9, 32, 20, 16, 2, EDGE)
    for x, length in ((13, 8), (16, 6), (20, 8), (25, 8)):
        s.line([face(x, 36), face(x, 36 + length)], EDGE)
    s.line([face(11, 24), face(27, 24)], DETAIL)
    badge(s, "check", *face(37, 11), 11)
