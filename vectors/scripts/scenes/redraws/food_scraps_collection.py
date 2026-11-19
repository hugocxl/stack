from geometry import EDGE
from scenes.redraws._w1 import upright_profile, wheelie_bin

DESCRIPTION = "An apple core protrudes from the opening of a wheeled organics bin."


def apple_core(s, x, y, z, scale):
    outline = [(-12, 52), (-13, 56), (-9, 60), (-5, 65), (-5, 70),
               (-10, 76), (-12, 82), (-8, 86), (0, 83), (8, 86),
               (13, 82), (11, 76), (6, 71), (5, 65), (9, 60),
               (13, 55), (12, 52), (6, 49), (0, 51), (-6, 49)]
    upright_profile(s, [(x + a * scale, z + b * scale) for a, b in outline],
                    y + 7 * scale, 4 * scale)

    def p(a, b, c):
        return (x + a * scale, y + b * scale, z + c * scale)

    s.tube([p(0, 6, 83), p(0, 6, 91), p(3, 6, 94)], 1.25 * scale)
    s.line([p(-2.6, 7, 63), p(-.6, 7, 67)], EDGE)
    s.line([p(.2, 7, 67), p(1.2, 7, 70)], EDGE)


def draw(s):
    wheelie_bin(s, 0, 0, contents=apple_core)
