from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w2 import rule, upright_face
from scenes.redraws._w4 import Surface, wrench_mark
from scenes.redraws.homebuyer_closing_packet import house_emblem

DESCRIPTION = "A warning triangle flags the top issue in a stack of house-marked maintenance tickets."


def draw(s):
    for dx, dy, dz in ((-8, -12, 11), (-4, -6, 5.5), (0, 0, 0)):
        def point(x, z):
            return .72*x + dx, -.28*x - .47*z + dy, .79*z + dz

        upright_face(s, point, rounded(0, 0, 93, 53, 5), 3)

    house_emblem(s, point, 24, 29, 14)
    rule(s, point, 44, 41, 19)
    wrench_mark(Surface(s, point), 53, 17, .44)
    s.line([point(71, 7), point(71, 46)], DETAIL, dashed=True)
    x, y, z = point(83, 26)
    warning(s, x + 1, y + 7, z + 2, 29)
