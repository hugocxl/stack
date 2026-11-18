from scenes.redraws._kit import badge
from scenes.redraws._w5 import place_setting

DESCRIPTION = "A dining table set for two carries a clock badge on the edge of its tabletop."


def draw(s):
    for x, y in ((5, 5), (49, 5), (5, 35), (49, 35)):
        s.box(x, y, 0, 4.5, 4.5, 30, .9)
    s.box(1, 1, 29, 56, 42, 5, 3)
    top = lambda x, y: (x, y, 34)
    for x, y in ((16, 13), (39, 29)):
        place_setting(s, top, x, y, 6.5)
    badge(s, "clock", 56, 15, 40, 10.5)
