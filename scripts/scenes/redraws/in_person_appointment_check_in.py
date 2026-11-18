from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w4 import front_surface, upright
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A floor-standing clinic check-in kiosk shows an identity card above its contactless reader and carries a check badge."


def draw(s):
    s.box(-6, -27, 0, 58, 44, 6, 6)
    s.box(11, -19, 6, 24, 21, 64, 4)
    angle = -8
    upright(s, rounded(-2, 56, 47, 49, 5), 5, 11, angle=angle)
    face = front_surface(s, angle=angle, y=5)
    face.frame(3, 61, 37, 39, 3)
    face.frame(8, 72, 27, 17, 2, EDGE)
    medical_cross(face, 15, 80.5, 3.5, EDGE)
    face.rows(22, 78, (8, 8), step=5)
    reader = front_surface(s, angle=0, y=2)
    reader.frame(17, 40, 12, 10, 2, DETAIL)
    glyph(s, "wifi", *reader.at(23, 45), 4, EDGE)
    badge(s, "check", *face.at(51, 87), 16)
