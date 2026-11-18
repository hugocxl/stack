from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, upright
from scenes.redraws.lab_results import vial_mark

DESCRIPTION = "A rigid specimen shipping case is marked with a vial and carries an outward arrow badge."


def draw(s):
    upright(s, rounded(0, 0, 90, 59, 5), 31, 31)
    s.tube([(28, 19, 59), (28, 19, 69), (33, 19, 74), (57, 19, 74),
            (62, 19, 69), (62, 19, 59)], 3.4, EDGE)
    face = Surface(s, lambda u, v: (u, 31, 59 - v))
    face.line([(1, 12), (89, 12)], DETAIL)
    for u in (11, 67):
        face.frame(u, 8, 12, 9, 2, EDGE)
    vial_mark(face, 31, 22, 28, EDGE)
    badge(s, "arrow", 93, 16, 44, 16)
