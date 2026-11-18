from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w2 import face_arrow, upright_face

DESCRIPTION = "A decision diamond splits a workflow into two paths, with a check badge at the approving exit."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x, z

    s.line([point(8, 36), point(46, 36)], EDGE)
    upright_face(s, point, oval(8, 36, 6, 6, count=32)[:-1], 2)
    upper = [(58, 51), (58, 67), (64, 74), (115, 74)]
    lower = [(58, 22), (58, 5), (64, -2), (113, -2)]
    s.line([point(x, z) for x, z in upper], EDGE)
    face_arrow(s, point, lower, DETAIL, head=7)
    upright_face(s, point, [(40, 36), (58, 19), (76, 36), (58, 53)], 4)
    badge(s, "check", *point(115, 74), 15)
