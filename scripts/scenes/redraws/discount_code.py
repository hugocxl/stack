from geometry import BOLD, EDGE, oval
from scenes.redraws._w1 import barcode, price_tag

DESCRIPTION = "A merchandise tag bears a large percent sign above a short barcode."


def draw(s):
    price_tag(s, -45, 0, 0, 82)
    s.line([(1, 0, 18), (21, 0, 39)], BOLD)
    for x, z in ((2, 35), (20, 22)):
        s.line([(u, 0, v) for u, v in oval(x, z, 4.8, 4.8, count=24)], BOLD)
    barcode(s, -8, 0, 4, 35, 11)
    s.line([(-31, 0, 24), (-43, 1, 25), (-54, -4, 27), (-58, -12, 31),
            (-54, -18, 36), (-45, -16, 36), (-36, -8, 31), (-31, 0, 24)], EDGE)
