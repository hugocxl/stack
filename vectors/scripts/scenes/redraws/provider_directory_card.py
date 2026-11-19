from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import front_surface, stethoscope_mark, upright
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A clinician directory credential shows a stethoscope beside a medical cross and two specialty lines."


def draw(s):
    angle = -28
    upright(s, rounded(0, 0, 98, 63, 6), 4, 7, angle=angle)
    face = front_surface(s, angle=angle, y=4)
    face.frame(38, 54, 22, 4, 2, EDGE)
    face.frame(8, 10, 33, 36, 3)
    stethoscope_mark(face, 23, 29, .90, BOLD)
    medical_cross(face, 55, 37, 5, EDGE)
    face.rows(50, 17, (28, 37), step=8, ink=EDGE)
