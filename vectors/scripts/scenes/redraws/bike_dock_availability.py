from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A row of three bike docks stands on a base plate, and the empty one carries a check badge."


def draw(s):
    s.box(-60, -10, 0, 120, 20, 4, 2)
    for x in (-40, 0, 40):
        s.box(x - 6, -5, 4, 12, 10, 34, 3)
        s.box(x - 7, -6, 38, 14, 12, 4, 2)
    s.line([(-40, 5.1, 24), (-40, 5.1, 30)], EDGE)
    badge(s, "check", 40, 0, 62, 12)
