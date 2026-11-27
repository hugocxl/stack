from geometry import EDGE
from scenes.redraws._sf import seedling

DESCRIPTION = "A raised crop row of seedlings has an inspection arrow running along its side."


def draw(s):
    s.box(-70, -16, 0, 120, 30, 14, 3)
    for x in (-54, -30, -6, 18):
        seedling(s, x, 0, 14, 20)
    s.face([(-70, 26, .2), (40, 26, .2), (40, 21, .2), (56, 30, .2), (40, 39, .2), (40, 34, .2), (-70, 34, .2)], EDGE)
