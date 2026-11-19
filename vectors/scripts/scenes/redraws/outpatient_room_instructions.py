from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import Surface, upright
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A freestanding clinic wayfinding sign pairs a medical cross and room field with a right arrow."


def draw(s):
    s.box(15, -7, 0, 76, 29, 5, 5)
    for x in (26, 74):
        s.box(x, 5, 5, 6, 7, 59, 1)
    upright(s, rounded(0, 33, 106, 43, 5), 13, 9)
    face = Surface(s, lambda u, v: (u, 13, v))
    medical_cross(face, 21, 54, 11)
    face.frame(40, 45, 24, 18, 1.5)
    face.rows(45, 54, (14,), ink=EDGE)
    face.line([(71, 42), (71, 67)], DETAIL)
    glyph(s, "arrow", 87, 13, 54, 15)
