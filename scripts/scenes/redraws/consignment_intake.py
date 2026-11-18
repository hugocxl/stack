from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import barcode, price_tag

DESCRIPTION = "A looped consignment tag bears an inventory barcode and an attached plus badge."


def draw(s):
    eye = price_tag(s, -41, 0, 0, 78)
    x, y, z = eye
    s.tube([eye, (x - 12, y - 1, z + 2), (x - 20, y - 6, z + 5),
            (x - 23, y - 14, z + 10), (x - 20, y - 20, z + 13),
            (x - 14, y - 21, z + 13), (x - 7, y - 10, z + 7), eye], .8, EDGE)
    barcode(s, -12, 0, 7, 39, 15)
    for height, width in ((31, 20), (26, 15)):
        s.line([(-12, 0, height), (-12 + width, 0, height)], DETAIL)
    badge(s, "plus", -4, -7, 41, 13)
