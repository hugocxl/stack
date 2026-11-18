from geometry import EDGE
from scenes.redraws._w2 import rule, speech_bubble

DESCRIPTION = "A threaded connector runs from an original speech bubble to its smaller indented reply."


def draw(s):
    def point(x, z):
        return .73*x, -.27*x, z

    s.line([point(23, 43), point(23, 20), point(28, 15), point(53, 15)], EDGE)
    for x, z, width, height, lines in (
        (0, 49, 87, 43, ((28, 56), (15, 41))),
        (40, 0, 72, 36, ((23, 46), (12, 34))),
    ):
        def bubble(u, v):
            return point(x + u, z + v)

        speech_bubble(s, bubble, width, height, depth=5)
        for row, length in lines:
            rule(s, bubble, 11, row, length, EDGE)
