from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import clipboard, rect

DESCRIPTION = "A clipped consent form carries an X badge at its signature field."


def draw(s):
    face = clipboard(s, 53, 68)
    for z, width in ((46, 28), (38, 34), (30, 24)):
        s.line([face(10, z), face(10 + width, z)], DETAIL)
    rect(s, face, 9.5, 10, 33, 13, 1, EDGE)
    signature = [(13, 15), (17, 20), (17, 13), (22, 17), (24, 15), (31, 15)]
    s.line([face(x, z) for x, z in signature], EDGE)
    badge(s, "x", *face(45, 17), 12)
