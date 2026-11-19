from geometry import EDGE
from scenes.redraws._w4 import magazine

DESCRIPTION = "A bound magazine with a landscape cover is wrapped with a ribbon tied in a bow."


def draw(s):
    cover = magazine(s)
    cover.slab([(48, 0), (56, 0), (56, 99), (48, 99)], 6)
    cover.slab([(0, 58), (75, 58), (75, 66), (0, 66)], 6)
    for loop in (
        [(52, 62), (44, 58), (35, 50), (35, 45), (41, 44), (48, 48), (52, 59)],
        [(52, 62), (58, 51), (66, 49), (72, 52), (70, 58), (62, 62)],
    ):
        cover.slab(loop, 1, EDGE)
    cover.oval(52, 62, 3, 3, EDGE)
    cover.line([(50, 65), (43, 74), (37, 76)], EDGE)
    cover.line([(54, 65), (61, 73), (63, 78)], EDGE)
