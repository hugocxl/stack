from geometry import EDGE, oval
from scenes.redraws._w2 import rule, speech_bubble, upright_face

DESCRIPTION = "A flared notification bell overlaps the upper corner of a discussion bubble."


def discussion_bell(s):
    def bubble(x, z):
        return .72*x, -.28*x, z

    speech_bubble(s, bubble, 102, 59, depth=7)
    for z, length in ((40, 50), (28, 61), (16, 41)):
        rule(s, bubble, 15, z, length, EDGE)

    def bell(x, z):
        return bubble(96 + x, 56 + z)

    upright_face(s, bell, oval(0, -15, 4.8, 4.6, count=28)[:-1], 3)
    bell_body = [(-18, -11), (-18, -7), (-14, -4), (-12, 0), (-11, 8),
                 (-8, 14), (-4, 17), (4, 17), (8, 14), (11, 8), (12, 0),
                 (14, -4), (18, -7), (18, -11)]
    s.tube([bell(0, 15), bell(0, 19)], 2.3)
    upright_face(s, bell, bell_body, 4)
    rule(s, bell, -15, -6, 30, EDGE)
    return bell


def draw(s):
    discussion_bell(s)
