from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "An upright membership pass shows a star seal and a date box with an attached renewal badge."


def member_pass(s, origin=(0, 0, 0), *, width=94, height=59, lean=.22):
    """A plastic membership pass standing on its long edge."""
    face = Surface(s, origin, rise=(-lean, 1), back=(0, -1, -lean))
    face.plate(rounded(0, 0, width, height, 5), 5)
    return face


def draw(s):
    face = member_pass(s, width=66, height=90, lean=.33)
    face.rect(25, 78, 16, 4.5, 2, EDGE)
    face.oval(33, 56, 13, 13)
    printed_glyph(face, "star", 33, 56, 11)
    face.rect(15, 13, 33, 24, 2, EDGE)
    face.rules(16, 29, [31], ink=EDGE)
    for x in (23, 40):
        face.stroke([(x, 35), (x, 40)], EDGE)
    face.rules(23, 22, [5])
    face.rules(34, 22, [5])
    badge(s, "refresh", *face.point(68, 20, -4), 15)
