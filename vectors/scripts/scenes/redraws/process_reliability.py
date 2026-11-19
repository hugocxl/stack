from geometry import EDGE, oval, rounded
from scenes.redraws._kit import arrow, badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A raised start node, process block, and decision diamond lead to a final block with a check badge."


def draw(s):
    flow = front_surface(s, angle=-27, z=5)
    flow.slab(oval(21, 69, 17, 11)[:-1], 5)
    flow.slab(rounded(66, 57, 33, 24, 4), 5)
    flow.slab([(82.5, 12), (99, 25), (82.5, 38), (66, 25)], 5)
    flow.slab(rounded(4, 13, 34, 24, 4), 5)

    for start, end in (((39, 69), (64, 69)), ((82.5, 55), (82.5, 40)),
                       ((64, 25), (40, 25))):
        arrow(s, [flow.at(*start), flow.at(*end)], EDGE, head=5.5)
    badge(s, "check", *flow.at(7, 18), 12)
