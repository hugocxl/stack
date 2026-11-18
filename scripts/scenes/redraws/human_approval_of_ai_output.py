from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import rule, sparkle, speech_bubble

DESCRIPTION = "An AI response bubble has a sparkle in its header and an attached approval check badge."


def draw(s):
    def p(x, z):
        return .24*x, -.76*x - .08*z, z

    speech_bubble(s, p, 108, 74, depth=8)
    sparkle(s, p, 20, 54, 9, EDGE)
    rule(s, p, 36, 54, 44, EDGE)
    for z, length in ((38, 71), (28, 62), (18, 42)):
        rule(s, p, 15, z, length, DETAIL)
    badge(s, "check", *p(105, 59), 14)
