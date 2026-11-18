from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import speech_bubble

DESCRIPTION = "A rounded message bubble with short lines carries a check badge on its lower-right corner."


def message(s):
    def face(u, v):
        return .72*u, -.28*u - .19*v, v + 9

    speech_bubble(s, face, 75, 44, depth=6)
    for z, end, ink in ((31, 59, EDGE), (22, 50, DETAIL), (13, 39, DETAIL)):
        s.line([face(12, z), face(end, z)], ink)
    return face(76, 11)


def draw(s):
    badge(s, "check", *message(s), 12)
