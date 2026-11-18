from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import rule, speech_bubble

DESCRIPTION = "A check badge overlaps the upper corner of a speech bubble with three comment lines."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x, z

    speech_bubble(s, point, 103, 61, depth=8)
    for z, length in ((43, 52), (30, 62), (17, 37)):
        rule(s, point, 16, z, length, EDGE)
    badge(s, "check", *point(100, 57), 15)
