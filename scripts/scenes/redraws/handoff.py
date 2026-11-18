from geometry import BOLD, EDGE
from scenes.redraws._w2 import face_arrow, folded_sheet, rule

DESCRIPTION = "A single folded document passes between two binder clips, following a directional arrow."


def draw(s):
    def plane(x, z):
        return .79*x, -.21*x - .39*z, .87*z

    def page(x, z):
        return plane(x + 27, z + 4)

    def clip(x, z, side):
        def jaw(u, v, height=0):
            a, b, c = plane(x + side*u, z + v)
            return a + height*.28, b + height*.5, c + height

        wire = [(7, -7), (15, -5), (21, -6), (24, -4),
                (24, 4), (21, 6), (15, 5), (7, 7)]
        s.tube([jaw(u, v, .5) for u, v in wire], 1.0, EDGE)
        toes = [jaw(-5, -10), jaw(-5, 10)]
        heels = [jaw(10, -10, 8), jaw(10, 10, 8)]
        s.face([toes[0], heels[0], jaw(10, -10, -1)], EDGE)
        s.face([toes[0], heels[0], heels[1], toes[1]], EDGE)
        s.tube([jaw(u, v, 7) for u, v in wire], 1.0, EDGE)

    folded_sheet(s, page, 68, 81, fold=12, depth=4)
    rule(s, page, 13, 59, 36, EDGE)
    rule(s, page, 13, 47, 29)
    clip(27, 45, -1)
    clip(95, 26, 1)
    face_arrow(s, plane, [(41, 28), (81, 28)], BOLD, head=9)
