from geometry import EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "An over-ear headset with a boom microphone carries a clock badge for booking."


def draw(s):
    band = [(x, 0, z) for x, z in oval(0, 27, 28, 37, 180, 0, 32)]
    s.tube(band, 3.3)
    s.tube([(x, 0, z) for x, z in oval(0, 27, 25, 33, 143, 37, 24)], 4.0)
    for x in (-28, 28):
        s.box(x - 6, -9, 3, 12, 18, 24, 5)
        s.line([(x + 1, 9, 7), (x + 1, 9, 22)])
    s.tube([(27, 8, 12), (24, 15, 8), (16, 20, 6), (6, 21, 6)], 1.8)
    s.tube([(5, 21, 6), (0, 21, 7)], 3, EDGE)
    badge(s, "clock", 29, 0, 62, 12)
