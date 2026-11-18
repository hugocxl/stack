from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, upright
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A standing medical envelope is sealed with a cross and carries an outward transfer arrow."


def draw(s):
    angle = -23
    upright(s, rounded(0, 0, 93, 61, 3), 2, 9, angle=angle)
    face = front_surface(s, angle=angle, y=2)
    face.line([(1, 58), (39, 31)], EDGE)
    face.line([(53, 31), (92, 58)], EDGE)
    face.line([(1, 3), (31, 29)])
    face.line([(62, 29), (92, 3)])
    medical_cross(face, 46.5, 31, 8, EDGE)
    badge(s, "arrow", *face.at(93, 47), 17)
