from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import upright

DESCRIPTION = "A support headset has a boom microphone and a clock badge tucked against its headband."


def draw(s):
    outer = oval(0, 24, 35, 41, 180, 0, 36)
    inner = oval(0, 24, 29, 34, 0, 180, 36)
    upright(s, outer + inner, 0, 8, BOLD)

    for x in (-32, 32):
        upright(s, rounded(-10, 2, 20, 26, 9), x + 7, 14, angle=-90)
        s.line([(x + 7, y, z) for y, z in oval(0, 15, 6, 8, count=32)], DETAIL)

    s.tube([(32, 9, 12), (30, 14, 8), (24, 18, 5), (14, 20, 5)], 1.6)
    s.tube([(14, 20, 5), (8, 20, 5)], 3, EDGE)

    badge(s, "clock", 17, 5, 56, 14)
