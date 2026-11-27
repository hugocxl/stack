from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.sleep_tracking import smartwatch

DESCRIPTION = "A smartwatch shows a pulse trace on its screen and carries a lock badge."


def draw(s):
    screen = smartwatch(s)
    screen.line([(-13, 33), (-8, 33), (-5, 39), (-1, 27), (3, 44), (7, 33), (13, 33)], EDGE)
    badge(s, "lock", *screen.at(22, 12), 13)
