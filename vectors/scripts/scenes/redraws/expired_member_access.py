from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A membership pass shows a crossed-out date box beside an attached clock badge."


def membership_pass(s, *, origin=(0, 0, 0)):
    face = Surface(s, origin, rise=(-.49, .87), back=(0, -.87, -.49))
    face.plate(rounded(0, 0, 98, 61, 6), 5)
    return face


def member_emblem(face, x, v, size):
    """An embossed membership seal with a star at its center."""
    face.oval(x, v, size, size, EDGE)
    printed_glyph(face, "star", x, v, size * .77)


def draw(s):
    face = membership_pass(s)
    member_emblem(face, 23, 34, 13)
    face.rules(43, 46, [32], ink=EDGE)
    face.rect(45, 13, 23, 22, 2, EDGE)
    face.rules(45, 28, [23], ink=EDGE)
    for x in (51, 62):
        face.stroke([(x, 31), (x, 38)], EDGE)
    printed_glyph(face, "slash", 57, 20, 8)
    badge(s, "clock", 95, -13, 44, 15)
