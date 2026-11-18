from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, desk_sheet, face_arrow, rule, upright_face

DESCRIPTION = "An arrow carries one selected region out of a folded document as a clipped excerpt."


def draw(s):
    point = desk_sheet(s, 85, 103)
    for z, width in ((82, 49), (71, 54), (59, 42), (21, 50), (12, 35)):
        rule(s, point, 12, z, width)
    closed_outline(s, point, rounded(10, 31, 38, 19, 2), EDGE)
    for z, width in ((43, 27), (37, 20)):
        rule(s, point, 16, z, width, EDGE)

    def excerpt(x, z):
        return point(x + 110, z + 32)

    upright_face(s, excerpt, rounded(0, 0, 38, 19, 2), 4)
    rule(s, excerpt, 6, 12, 27, EDGE)
    rule(s, excerpt, 6, 6, 20, DETAIL)
    face_arrow(s, point, [(49, 40), (102, 40)], head=10)
