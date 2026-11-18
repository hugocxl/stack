from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import printed_stroke, rect

DESCRIPTION = "A food-package label shows a peanut and ingredient lines, with a check next to the allergen row."


def draw(s):
    s.box(0, 0, 0, 65, 23, 51, 3)
    s.box(0, 0, 48, 65, 23, 4, 2)
    label = lambda x, z: (x, 23, z)
    rect(s, label, 5, 6, 54, 37, 2, EDGE)
    peanut = [(-1, 10), (-5, 8), (-6, 4), (-4, 0), (-5, -3), (-5, -7),
              (-2, -9), (2, -9), (5, -6), (5, -3), (3, 1), (5, 5),
              (4, 8), (2, 10), (-1, 10)]
    printed_stroke(s, label, [(16 + u, 26 + v) for u, v in peanut], EDGE)
    for u, v in ((15, 19), (18, 22), (15, 30), (17, 33)):
        printed_stroke(s, label, [(u - 1, v), (u + 1, v + .5)], DETAIL)
    printed_stroke(s, label, [(27, 34), (52, 34)], DETAIL)
    printed_stroke(s, label, [(27, 25), (47, 25)], BOLD)
    printed_stroke(s, label, [(27, 16), (47, 16)], DETAIL)
    badge(s, "check", *label(58, 25), 7.7)
