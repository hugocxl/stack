from geometry import EDGE
from scenes.redraws._w1 import server_tower, upright_profile
from scenes.systems_shapes import bezel

DESCRIPTION = "A small house emblem is mounted above the drive bays of a server tower."


def draw(s):
    server_tower(s)
    house = [(-14, 36), (-14, 46), (-18, 46), (0, 59),
             (18, 46), (14, 46), (14, 36)]
    upright_profile(s, house, 2, 3)
    bezel(s, -4, 2, 36.5, 8, 9, EDGE, .6)
