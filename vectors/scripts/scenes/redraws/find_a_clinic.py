from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A location pin marked with a medical cross stands on a folded street map."


def medical_cross(face, u, v, radius, ink=EDGE):
    arm = radius / 3
    outline = [(-arm, radius), (arm, radius), (arm, arm), (radius, arm),
               (radius, -arm), (arm, -arm), (arm, -radius), (-arm, -radius),
               (-arm, -arm), (-radius, -arm), (-radius, arm), (-arm, arm)]
    face.outline([(u + x, v + y) for x, y in outline], ink)


def draw(s):
    folds = ((0, 18), (30, 0), (63, 23), (94, 4))
    for (x, z), (u, v) in zip(folds, folds[1:]):
        s.face([(x, 63, z), (u, 63, v), (u, 63, v + 2), (x, 63, z + 2)], DETAIL)
        s.face([(x, 0, z + 2), (u, 0, v + 2), (u, 63, v + 2), (x, 63, z + 2)])
    s.line([(0, 15, 20), (30, 20, 2), (63, 17, 25), (94, 22, 6)], DETAIL)
    s.line([(8, 0, 15.2), (26, 32, 4.4), (30, 40, 2), (63, 42, 25),
            (94, 39, 6)], DETAIL)
    s.line([(47, 0, 13.85), (47, 41, 13.85), (58, 63, 21.5)], DETAIL)
    s.line([(80, 0, 14.6), (76, 40, 17), (80, 63, 14.6)], DETAIL)

    x, y, tip = 64, 27, 24.4
    upright(s, [(x, tip), *oval(x, tip + 36, 19, 19, -35, 215, 45)], y, 4, EDGE)
    medical_cross(Surface(s, lambda u, v: (u, y, v)), x, tip + 36, 10, BOLD)
