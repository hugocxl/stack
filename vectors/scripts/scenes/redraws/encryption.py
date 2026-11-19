from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A data block engraved with scrambled rows of dots and dashes carries a padlock badge."


def draw(s):
    s.box(0, 0, 0, 67, 16, 42, 4)
    rows = (
        (32, ((10, 7), (22, 1.3), (29, 10), (45, 1.3), (52, 5))),
        (22, ((10, 1.3), (17, 12), (34, 1.3), (41, 6))),
        (12, ((10, 5), (21, 1.3), (28, 8), (42, 1.3))),
    )
    for z, marks in rows:
        for x, length in marks:
            s.line([(x, 16, z), (x + length, 16, z)], EDGE)
    badge(s, "lock", 65, 18, 17, 17)
