from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import upright

DESCRIPTION = "A notification bell with a visible clapper carries a refresh badge at its upper rim."


def draw(s):
    s.tube([(3, 10, 15), (3, 10, 23)], 8, EDGE)
    outline = [(-39, 21), (-39, 27), (-32, 32), (-28, 41), (-26, 61),
               (-23, 73), (-16, 82), (-8, 87), (8, 87), (16, 82),
               (23, 73), (26, 61), (28, 41), (32, 32), (39, 27), (39, 21)]
    upright(s, outline, 13, 16, angle=-26)
    s.line([(x * .8988 + 13 * .4384, 13 * .8988 - x * .4384, 27)
            for x in (-36, 36)], EDGE)
    s.line([(x, 2, z) for x, z in oval(0, 85, 8, 10, 0, 180, 20)], EDGE)
    badge(s, "refresh", 31, -7, 74, 17)
