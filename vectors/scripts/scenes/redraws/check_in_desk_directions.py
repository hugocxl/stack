from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import plane_mark

DESCRIPTION = "An airport check-in counter carries an airplane emblem and a desk bell above an approach arrow."


def draw(s):
    arrow(s, [(37, 57, 0), (37, 27, 0)], BOLD, head=9)
    s.box(0, 0, 0, 60, 22, 36, 2.6)
    s.box(-2, -2, 35, 64, 26, 5, 2)
    plane_mark(s, lambda x, z: (x, 22, z), 31, 19, .78)
    s.disk(16, 13, 40, 6, 5.5, 2)
    s.solid(oval(16, 13, 5.6, 5)[:-1], 42, 4.5,
            oval(16, 13, 2, 1.7)[:-1], crease=False)
    s.disk(16, 13, 46.5, 1.2, 1.2, 1.5)
