from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A curled tuition receipt has a mortarboard letterhead and a check badge beside its boxed total."


def draw(s):
    s.tube([(0, -4, 88), (61, -4, 88)], 5)
    receipt = Surface(s, (0, 5, 5), rise=(-.09, 1), back=(0, -1, -.09))
    tail = [(x, 0 if i % 2 == 0 else 4) for i, x in enumerate(range(0, 61, 6))]
    receipt.plate(tail + [(60, 83), (0, 83)], 2.5)
    cover_cap(receipt, 28, 67, 28)
    for v, width in ((50, 24), (41, 18), (32, 22)):
        receipt.rules(7, v, [width])
        receipt.rules(44, v, [9], ink=EDGE)
    receipt.rect(8, 10, 44, 12, 1, EDGE)
    receipt.rules(13, 16, [12])
    receipt.rules(36, 16, [10], ink=EDGE)
    badge(s, "check", *receipt.point(57, 17), 13)
