from geometry import DETAIL
from scenes.redraws._kit import badge

DESCRIPTION = "A thick concrete sample has exposed aggregate, a smooth finished margin, and a check badge."


def draw(s):
    s.box(-37, -26, 0, 74, 52, 12, 3)
    s.line([(25, -25.5, 12), (25, 25.5, 12)], DETAIL)
    chip = [(-.6, -.15), (-.14, -.5), (.49, -.24),
            (.6, .21), (.08, .53), (-.6, -.15)]
    for x, y, width, depth in (
        (-27, -17, 4, 2.2), (-13, -9, 3.1, 3.5), (-30, 1, 3.3, 1.8),
        (-22, 9, 4.5, 2.2), (-5, -20, 2.8, 3.8), (6, -12, 3.3, 1.8),
        (-7, 3, 4.6, 3), (1, 10, 2.2, 3), (12, 6, 2.8, 2.1),
        (18, -17, 4.4, 1.8), (20, -1, 2.8, 3.7), (21, 8, 3.6, 1.7),
        (22, -11, 2.5, 3.2),
    ):
        s.line([(x + u * width, y + v * depth, 12) for u, v in chip], DETAIL)
    for x, y in ((-9, -14), (0, -5), (-12, 12), (12, -22),
                 (15, -3), (21, 12), (7, 14), (-22, -4),
                 (-5, 22), (12, 19), (-23, 19)):
        s.line([(x, y, 12), (x + 1.8, y + .4, 12)], DETAIL)
    for x, z in ((-24, 6), (-11, 8), (3, 5), (17, 8)):
        s.line([(x, 26, z), (x + 2, 26, z - 1)], DETAIL)
    badge(s, "check", 39, -17, 14, 11)
