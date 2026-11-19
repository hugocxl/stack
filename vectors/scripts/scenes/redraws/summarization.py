from geometry import EDGE
from scenes.redraws._w2 import face_arrow, folded_sheet, rule

DESCRIPTION = "An arrow leads from three densely ruled pages to one smaller page with just two short lines."


def draw(s):
    def plane(x, z):
        return .77*x, -.23*x - .28*z, .93*z

    for offset in (16, 8, 0):
        def source(x, z):
            return plane(x + offset, z + offset)

        folded_sheet(s, source, 51, 75, fold=9, depth=2.5)
    for z, size in ((57, 27), (47, 35), (37, 31), (27, 35), (17, 23)):
        rule(s, source, 8, z, size, EDGE)

    def summary(x, z):
        return plane(x + 98, z + 8)

    folded_sheet(s, summary, 39, 53, fold=9, depth=3)
    for z, length in ((31, 23), (22, 16)):
        rule(s, summary, 8, z, length, EDGE)
    face_arrow(s, plane, [(64, 39), (90, 39)], head=8)
