from math import sqrt

from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import coin
from scenes.redraws._w3 import Surface

DESCRIPTION = "A circular contrast dial sets a dark, striped semicircle directly beside an open semicircle."


def draw(s):
    coin(s, 0, 0, 0, 38, depth=7)
    dial = Surface(s, (0, .02, 0))
    dial.stroke(oval(0, 0, 30, 30, 270, 450, 32), EDGE)
    dial.stroke(oval(0, 0, 30, 30, 90, 270, 32), BOLD)
    dial.stroke([(0, -30), (0, 30)], BOLD)
    for z in (-18, -6, 6, 18):
        dial.stroke([(-sqrt(30 ** 2 - z ** 2) + 3, z), (-3, z)], BOLD)
