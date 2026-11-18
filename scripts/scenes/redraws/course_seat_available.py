from geometry import rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import upright

DESCRIPTION = "A classroom chair has a plus badge at the upper-right corner of its backrest."


def draw(s):
    # The rear legs continue through the seat to support the backrest.
    s.tube([(1, -2, 0), (7, 4, 34), (7, 1, 63)], 1.75)
    s.tube([(46, 1, 0), (42, 4, 34), (42, 1, 63)], 1.75)
    s.tube([(2, 38, 0), (7, 30, 34)], 1.75)
    s.tube([(47, 38, 0), (42, 30, 34)], 1.75)
    s.box(0, 0, 31, 49, 35, 4, 5)

    backrest = rounded(1, 54, 47, 23, 6)
    handle = rounded(16, 65, 17, 5, 2.5)
    s.face(upright(backrest, -1.5), openings=[upright(handle, -1.5)])
    s.face(upright(backrest, 1), openings=[upright(handle, 1)])

    badge(s, "plus", 49, 0, 72, 12)
