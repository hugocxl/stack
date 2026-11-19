from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, upright
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A clinic hours sign on a single post displays a medical cross above ruled time slots and carries a clock badge."


def draw(s):
    s.disk(35, -9, 0, 17, 13, 5)
    s.box(31, -12, 5, 8, 7, 48, 2)
    angle = -17
    upright(s, rounded(0, 35, 73, 59, 5), 4, 8, angle=angle)
    face = front_surface(s, angle=angle, y=4)
    medical_cross(face, 36.5, 78, 10, EDGE)
    face.line([(8, 63), (61, 63)])
    for v in (48, 55):
        face.rows(13, v, (15,), ink=EDGE)
        face.rows(36, v, (14,))
    badge(s, "clock", *face.at(71, 73), 15)
