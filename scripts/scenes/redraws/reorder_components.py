from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "A middle row shifts out of a three-row list beside a tall, two-ended reorder arrow."


def draw(s):
    for x, y, z, ink in ((0, 0, 63, EDGE), (0, 0, 0, EDGE), (12, -3, 32, BOLD)):
        row = Surface(s, (x, y, z), across=(.96, -.28))
        row.plate(rounded(0, 0, 76, 22, 4), 5, ink)
        for v in (7, 11, 15):
            row.rules(8, v, [7], ink=EDGE)
        row.rules(24, 11, [33], ink=DETAIL)

    arrow(s, [(102, -19, 28), (102, -19, 76)], EDGE, head=10)
    arrow(s, [(102, -19, 52), (102, -19, 28)], EDGE, head=10)
