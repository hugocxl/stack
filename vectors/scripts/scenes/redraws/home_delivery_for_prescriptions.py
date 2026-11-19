from geometry import BOLD, EDGE
from scenes.redraws._w4 import Surface, capsule_mark
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A taped delivery parcel has a prominent capsule and a small medical cross on its front label."


def draw(s):
    s.box(-25, -19, 0, 50, 38, 35, 2)
    for x in (0, 8):
        s.line([(x, -18, 35), (x, 19, 35), (x, 19, 29)], EDGE)
    s.line([(0, 19, 29), (8, 19, 29)], EDGE)
    label = Surface(s, lambda u, v: (u, 19, v))
    label.frame(-18, 4, 36, 21, 2, EDGE)
    capsule_mark(label, -5, 14, 10, BOLD)
    medical_cross(label, 10, 14, 4, EDGE)
