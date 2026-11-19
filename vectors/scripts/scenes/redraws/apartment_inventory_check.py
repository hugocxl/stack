from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule, upright_face
from scenes.redraws.homebuyer_closing_packet import house_emblem

DESCRIPTION = "A gridded apartment inventory card lists a chair and lamp beneath a house emblem with a check badge."


def draw(s):
    def point(x, z):
        return .68*x, -.32*x - .32*z, .92*z

    upright_face(s, point, rounded(0, 0, 76, 79, 4), 6)
    house_emblem(s, point, 37, 62, 12)
    closed_outline(s, point, [(9, 9), (65, 9), (65, 45), (9, 45)], EDGE)
    for x in (30, 52):
        s.line([point(x, 9), point(x, 45)], DETAIL)
    rule(s, point, 9, 27, 56)
    s.line([point(15, 30), point(15, 43), point(21, 43), point(21, 35),
            point(25, 35), point(25, 30)], EDGE)
    closed_outline(s, point, [(15, 17), (18, 24), (22, 24), (25, 17)], EDGE)
    s.line([point(20, 17), point(20, 12)], EDGE)
    rule(s, point, 17, 12, 6, EDGE)
    for z in (18, 36):
        rule(s, point, 34, z, 14)
        rule(s, point, 56, z, 5)
    x, y, z = point(74, 64)
    badge(s, "check", x + 3, y, z, 14)
