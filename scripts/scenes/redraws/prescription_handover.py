from geometry import DETAIL, EDGE
from scenes.redraws._w4 import Surface, capsule_mark, pharmacy_bottle

DESCRIPTION = "A capped prescription bottle protrudes from a gusseted pharmacy pickup bag with a loop handle."


def draw(s):
    back = [(-28, -13, 0), (28, -13, 0), (29, -15, 40), (-29, -15, 40)]
    front = [(-28, 13, 0), (28, 13, 0), (30, 17, 35), (-30, 17, 35)]
    s.face(back)
    s.face([back[0], front[0], front[-1], back[-1]], DETAIL)
    s.tube([(-17, -15, 39), (-17, -15, 48), (-14, -15, 54),
            (-9, -15, 57), (-3, -15, 57), (2, -15, 54),
            (5, -15, 48), (5, -15, 39)], 1.65)
    label = pharmacy_bottle(s, 6, -1, 24, 1)
    capsule_mark(label, 0, 22, 10, EDGE)
    s.face([back[1], front[1], front[2], back[2]])
    s.line([(28, 13, 0), (28.5, 0, 18), (29.5, .5, 37)], DETAIL)
    s.face(front)
    s.tube([(-24, 17, 35), (-24, 19, 43), (-21, 20, 49),
            (-16, 20, 51), (-11, 20, 50), (-7, 19, 44),
            (-7, 17, 35)], 1.65)
    face = Surface(s, lambda u, v: (u, 13 + v*4/35, v))
    face.frame(-12, 9, 24, 15, 2)
    face.rows(-7, 16, (14,), ink=EDGE)
