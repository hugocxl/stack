from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, rule, upright_face
from scenes.redraws.move_in_checklist import key_outline

DESCRIPTION = "A tenant folder contains welcome papers and a key tucked into its house-shaped front pocket."


def draw(s):
    def point(x, z):
        return x, -.32*z, .87*z

    upright_face(s, point, [(0, 0), (90, 0), (90, 61), (39, 61),
                            (33, 71), (0, 71)], 5)
    upright_face(s, point, [(12, 34), (80, 34), (80, 76), (12, 76)], 2)
    rule(s, point, 21, 66, 39, DETAIL)
    rule(s, point, 21, 57, 25, DETAIL)

    def cover(x, z):
        a, b, c = point(x, z)
        return a, b + 5, c

    upright_face(s, cover, [(0, 0), (90, 0), (90, 48), (0, 48)], 4)

    def key(u, v):
        return cover(51 + u*.76 + v*.65, 44 - u*.65 + v*.76)

    key_outline(s, key, 0, 0, 22)
    pocket = [(25, 6), (67, 6), (67, 27), (46, 42), (25, 27)]
    # The pocket masks the portion of the key that is tucked inside it.
    s.face([cover(x, z) for x, z in pocket], EDGE)
    chart_line(s, cover, [(29, 23), (29, 11), (63, 11), (63, 23)], DETAIL)
    chart_line(s, cover, [(43, 12), (43, 19), (50, 19), (50, 12)], DETAIL)
