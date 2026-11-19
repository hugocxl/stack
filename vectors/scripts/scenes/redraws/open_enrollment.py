from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A school doorway with a mortarboard above its opening has an open door and a plus badge."


def draw(s):
    frame = Surface(s, (0, 0, 0))
    for x in (0, 64):
        s.box(x, -11, 0, 11, 11, 78, 1)
    s.box(0, -11, 77, 75, 11, 22, 2)
    cover_cap(frame, 38, 88, 26, EDGE)
    s.box(2, -11, 0, 71, 14, 3, 1)

    leaf = Surface(s, (11, 0, 3))
    # The open leaf swings toward the viewer from its left hinge.
    def point(u, v):
        return leaf.point(u * .46, v, -u * .89)

    s.face([point(u, v) for u, v in ((0, 0), (52, 0), (52, 72), (0, 72))])
    s.face([point(u, v) for u, v in ((8, 39), (44, 39), (44, 64), (8, 64))])
    s.face([point(u, v) for u, v in ((8, 8), (44, 8), (44, 26), (8, 26))])
    s.tube([point(44, 32), point(49, 32)], 1.4)
    badge(s, "plus", 72, 5, 73, 14)
