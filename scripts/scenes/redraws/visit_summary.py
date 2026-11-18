from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import Surface, front_surface
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A clinical summary sheet sits in a medical report binder with a cross in its header."


def draw(s):
    cover = front_surface(s, angle=-29, z=6, lean=.51)
    cover.slab(rounded(0, 0, 82, 87, 4), 6)
    spine = Surface(s, lambda u, v: cover.at(u - 3, v + 1))
    spine.slab(rounded(0, 0, 12, 85, 3), 5)
    cover.slab(rounded(12, 7, 63, 73, 3), 2)
    medical_cross(cover, 25, 64, 8.5, BOLD)
    cover.rows(39, 66, (23, 16), step=-6)
    cover.line([(17, 51), (69, 51)], EDGE)
    for v in (37, 24):
        cover.rows(20, v, (14,), ink=EDGE)
        cover.rows(41, v, (22,))
