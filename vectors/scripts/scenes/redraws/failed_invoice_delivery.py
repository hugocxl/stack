from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import invoice, printed_stroke

DESCRIPTION = "An itemized invoice emerges from an open envelope with a cross badge on the lower corner."


def draw(s):
    back = lambda x, z: (x, -12, z)
    s.face([back(0, 36), back(36, 57), back(77, 36), back(77, 0), back(0, 0)], EDGE)

    invoice(s, in_envelope=True)

    front = lambda x, z: (x, 5, z)
    s.face([back(77, 36), front(77, 36), front(77, 0), back(77, 0)], EDGE)
    s.face([front(0, 0), front(77, 0), front(77, 36), front(39, 14), front(0, 36)], EDGE)
    printed_stroke(s, front, [(0, 0), (19.5, 25)], DETAIL)
    printed_stroke(s, front, [(77, 0), (58, 25)], DETAIL)
    badge(s, "x", *front(74, 8), 11.5)
