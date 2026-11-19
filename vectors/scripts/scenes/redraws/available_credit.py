from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import upright_card
from scenes.systems_shapes import bezel

DESCRIPTION = "A chipped credit card has a partially filled balance bar along its lower edge."


def draw(s):
    upright_card(s, 80, 50, 5, 3)
    bezel(s, 10, 0, 26, 16, 13, EDGE, 2)
    s.line([(10, 0, 32.5), (26, 0, 32.5)], DETAIL)
    for x in (15, 21):
        s.line([(x, 0, 26), (x, 0, 39)], DETAIL)
    for x, width in ((39, 12), (57, 12)):
        s.line([(x, 0, 30), (x + width, 0, 30)], DETAIL)

    bezel(s, 10, 0, 9, 60, 10, EDGE, 2)
    s.line([(47, 0, 9), (47, 0, 19)], BOLD)
    for x in (12, 18, 24, 30, 36):
        s.line([(x, 0, 9), (x + 7, 0, 19)], DETAIL)
