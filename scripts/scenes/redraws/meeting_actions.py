from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import SurfaceStrokes, closed_outline, rule, upright_face

DESCRIPTION = "A clipboard holds three action items, with check marks in the first two boxes."


def draw(s):
    def point(x, z):
        return .67*x, -.33*x - .50*z, .79*z

    upright_face(s, point, rounded(0, 0, 80, 101, 5), 8)
    upright_face(s, point, rounded(6, 6, 68, 87, 1), 1.4, DETAIL)

    def clip(x, z):
        a, b, c = point(x, z)
        return a, b + 2.6, c

    upright_face(s, clip, rounded(25, 86, 30, 16, 5), 3)
    rule(s, clip, 33, 96, 14, DETAIL)

    for z, width in ((66, 31), (43, 24), (20, 29)):
        closed_outline(s, point, rounded(15, z - 7, 15, 14, 2), EDGE)
        rule(s, point, 38, z + 2, width, EDGE)
        rule(s, point, 38, z - 5, width*.58, DETAIL)
    page = SurfaceStrokes(s, point)
    for z in (66, 43):
        glyph(page, "check", 22, 0, z, 6)
