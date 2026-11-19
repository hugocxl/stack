from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w1 import fingerprint

DESCRIPTION = "A profile card shows a fingerprint and account details beside a clock badge."


def draw(s):
    s.box(-37, -3, 0, 74, 5, 45, 4)
    fingerprint(s, -19, 2.01, 23, 11.5)
    for z, width in ((30, 25), (22, 19), (14, 23)):
        s.line([(-2, 2.01, z), (-2 + width, 2.01, z)], DETAIL)

    badge(s, "clock", 34, 7, 44, 13)
