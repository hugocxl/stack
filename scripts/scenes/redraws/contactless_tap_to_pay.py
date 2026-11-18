from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import device, printed_stroke, rect

DESCRIPTION = "A smartphone touches the edge of a payment terminal next to its contactless wave mark."


def draw(s):
    face = lambda x, z: (x, 53 - .91 * z, z)
    s.face([(0, 3, 0), (51, 3, 0), (51, 3, 55), (0, 3, 55)], EDGE)
    s.face([(51, 3, 0), (51, 46, 0), face(51, 8), face(51, 55)], EDGE)
    s.face([(0, 46, 0), (51, 46, 0), face(51, 8), face(0, 8)], EDGE)
    s.face([face(0, 8), face(51, 8), face(51, 55), face(0, 55)], EDGE)
    rect(s, face, 6, 31, 38, 18, 2.1)
    glyph(s, "wifi", *face(32, 39), 13, EDGE)
    for x in (8, 20, 32):
        for z in (13, 21):
            rect(s, face, x, z, 8, 5, 1.2, DETAIL)
    phone = device(s, x=51, y=22, w=33, h=64)
    rect(s, phone, 7, 24, 19, 13, 2.1)
    rect(s, phone, 10, 29, 6, 4, .7, DETAIL)
    printed_stroke(s, phone, [(10, 27), (19, 27)], DETAIL)
