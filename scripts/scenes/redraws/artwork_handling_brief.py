from geometry import BOLD, EDGE
from scenes.redraws._w3 import clipboard

DESCRIPTION = "A clipboard shows a museum vase resting in a padded handling cradle above two instruction lines."


def draw(s):
    page = clipboard(s, w=81, h=91)
    page.stroke([(33, 62), (48, 62), (45, 58), (45, 53), (52, 48),
                 (53, 42), (49, 36), (32, 36), (28, 42), (29, 48),
                 (36, 53), (36, 58)], BOLD, closed=True)
    page.stroke([(20, 49), (20, 39), (26, 31), (55, 31), (61, 39), (61, 49),
                 (57, 49), (57, 41), (52, 36), (29, 36), (24, 41), (24, 49)],
                EDGE, closed=True)
    page.rules(18, 22, [45, 35], gap=7)
