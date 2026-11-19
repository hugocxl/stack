from geometry import EDGE
from scenes.editorial_objects import At, camera
from scenes.redraws._kit import badge

DESCRIPTION = "A camera stands on a splayed tripod with a plus badge beside its lens."


def draw(s):
    for x, y in ((18, 12), (11, 41), (59, 6)):
        s.tube([(x, y, 1.8), (27, 19, 49)], 2, EDGE)
    s.disk(27, 19, 48, 6, 6, 5)
    camera(At(s, 0, 0, 53))
    badge(s, "plus", 62, 31, 79, 11)
