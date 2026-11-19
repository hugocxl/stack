from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import database

DESCRIPTION = "A replication arrow points from a database cylinder to a second identical cylinder."


def draw(s):
    database(s, -29, 24, 20)
    database(s, 29, -24, 20)
    arrow(s, [(-11, 9, 17), (11, -9, 17)], BOLD, head=7)
