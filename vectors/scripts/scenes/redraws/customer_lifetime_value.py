from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import outline, profile_mark

DESCRIPTION = "A customer card peeks out of a wallet behind three progressively taller stacks of coins."


def draw(s):
    s.box(0, 0, 0, 111, 21, 56, 6)
    s.box(12, 7, 37, 69, 5, 39, 5)
    profile_mark(s, lambda x, z: (x, 12, z), 29, 62, 8)
    for z, end in ((64, 70), (58, 62)):
        s.line([(43, 12, z), (end, 12, z)], DETAIL)
    s.box(0, 17, 0, 111, 12, 48, 6)
    s.line([(6, 29, 38), (104, 29, 38)], DETAIL)
    s.box(77, 29, 21, 30, 5, 15, 4)
    outline(s, 92, 34, 25, 6, 6, 3, EDGE)

    for x, count in ((17, 1), (51, 3), (85, 5)):
        for coin in range(count):
            s.disk(x, 48, coin * 5, 13, 13, 5, BOLD if coin == count - 1 and count == 5 else EDGE)
        s.ellipse(x, 48, count * 5, 9, 9, DETAIL)
