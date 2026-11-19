from geometry import EDGE, GUIDE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A raised image block moves from the dashed slot on one page toward the facing page along a single arrow."


def draw(s):
    left = Surface(s, (0, 0, 0), rise=(-.48, .88), back=(0, -.88, -.48),
                   across=(.77, -.42))
    right = Surface(s, left.point(58, 0), rise=left.rise, back=left.back,
                    across=(.99, .12))
    for page in (left, right):
        page.plate(rounded(0, 0, 58, 69, 2), 4)
        page.rules(7, 60, [27], ink=EDGE)
        page.rules(7, 20, [41, 29], gap=8)
    left.stroke([(9, 28), (46, 28), (46, 50), (9, 50)], GUIDE, closed=True, dashed=True)

    block = Surface(s, left.point(34, 33, -12), rise=left.rise, back=left.back)
    block.plate(rounded(0, 0, 35, 25, 3), 4)
    photo_art(block, 4, 4, 27, 17)
    x, y, z = block.point(38, 12)
    arrow(s, [(x, y, z), (x + 23, y - 23, z)], EDGE, head=10)
