from geometry import DETAIL
from scenes.redraws._sf import carton

DESCRIPTION = "A shelving rack stands nearly empty, with a single carton left on its middle shelf."


def draw(s):
    W, D = 96, 30
    for x in (0, W - 3):
        s.box(x, 0, 0, 3, 3, 82, .8)
    for z in (0, 26, 52):
        s.box(0, 0, z + 4, W, D, 3, 1)
    carton(s, 58, 4, 33, 24, 22, 18, tape=False)
    for x in (0, W - 3):
        s.box(x, D - 3, 0, 3, 3, 82, .8)
