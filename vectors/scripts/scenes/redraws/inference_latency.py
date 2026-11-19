from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import rule, speech_bubble

DESCRIPTION = "A stopwatch overlaps the upper corner of a response bubble with three lines of output."


def draw(s):
    def point(x, z):
        return .71*x, -.29*x - .20*z, z

    speech_bubble(s, point, 101, 64, depth=8)
    for z, width in ((48, 48), (34, 64), (20, 49)):
        rule(s, point, 13, z, width, EDGE if z == 48 else DETAIL)
    x, y, z = point(95, 57)
    # The push button attaches above the viewer-facing clock badge.
    s.box(x - 6, y - 4, z + 22, 11, 7, 6, 2)
    badge(s, "clock", x, y, z, 20)
