from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.sleep_tracking import smartwatch

DESCRIPTION = "A smartwatch shows a pulse trace and carries a circular sync badge at its lower corner."


def draw(s):
    screen = smartwatch(s)
    screen.line([(-13, 34), (-8, 34), (-5, 39), (-1, 27),
                 (3, 44), (7, 34), (13, 34)], EDGE)
    badge(s, "refresh", *screen.at(22, 15), 13)
