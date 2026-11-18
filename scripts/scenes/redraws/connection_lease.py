from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import connector, database
from scenes.systems_shapes import bezel

DESCRIPTION = "A clock badge sits on the housing of a cable plugged into a database cylinder."


def draw(s):
    database(s, 0, -16, 25, pitch=10)
    bezel(s, -12, 8, 7, 24, 12, EDGE, 2)
    connector(s, 0, 19, 5)
    badge(s, "clock", 14, 23, 17, 12)
