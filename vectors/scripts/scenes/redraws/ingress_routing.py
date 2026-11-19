from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "Two incoming paths join before passing through a thick gateway arch."


def draw(s):
    rim = [(-27, 0), *oval(0, 24, 27, 25, 180, 0, 36), (27, 0)]
    opening = [(17, 0), *oval(0, 24, 17, 15, 0, 180, 28), (-17, 0)]
    upright_profile(s, rim + opening, 0, 13)
    for x in (-31, 23):
        s.line([(x, 31, 2), (x, 23, 2), (x * .8 - 1, 18, 2), (-7, 18, 2)], EDGE)
    arrow(s, [(-7, 18, 2), (-7, -14, 2)], BOLD, head=7)
