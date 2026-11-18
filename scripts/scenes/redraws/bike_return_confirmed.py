from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws.bike_share import bicycle

DESCRIPTION = "A city bicycle locks into a docking post with a check badge beside the latch."


def draw(s):
    bicycle(s)
    s.box(100, -29, 0, 9, 15, 3, 2)
    s.box(103, -26, 3, 7, 9, 33, 2)
    s.tube([(105, -21, 28), (91, -21, 28), (79, -20, 28)], 1.8)
    s.line([(106, -16.9, 29), (108, -16.9, 29)], DETAIL)
    badge(s, "check", 112, -24, 39, 10.5)
