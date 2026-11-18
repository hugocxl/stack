from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule, upright_face
from scenes.redraws.homebuyer_closing_packet import house_emblem

DESCRIPTION = "A building permit rests in a presentation folder with an embossed house emblem and a check badge."


def draw(s):
    def point(x, z):
        return .70*x, -.30*x - .58*z, .81*z

    upright_face(s, point, rounded(0, 0, 85, 69, 3), 9)
    closed_outline(s, point, [(6, 7), (79, 7), (79, 62), (6, 62)], EDGE)
    for x in (6, 79):
        u = 1 if x == 6 else -1
        for z in (7, 62):
            v = 1 if z == 7 else -1
            s.line([point(x, z + 10*v), point(x + 11*u, z)], DETAIL)
    house_emblem(s, point, 42, 42, 16)
    rule(s, point, 22, 22, 39, EDGE)
    rule(s, point, 29, 14, 25)
    x, y, z = point(86, 15)
    badge(s, "check", x, y + 3, z, 14)
