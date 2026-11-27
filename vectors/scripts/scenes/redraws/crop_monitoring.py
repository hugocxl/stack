from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import seedling

DESCRIPTION = "A raised crop bed of seedlings has a monitoring sensor on a post carrying a Wi-Fi badge."


def draw(s):
    s.box(-60, -16, 0, 100, 32, 14, 3)
    for x in (-44, -20, 4):
        seedling(s, x, 0, 14, 20)
    s.tube([(52, 0, 0), (52, 0, 46)], 1.6, EDGE)
    s.box(46, -6, 44, 12, 12, 12, 2.5)
    badge(s, "wifi", 72, -14, 74, 11)
