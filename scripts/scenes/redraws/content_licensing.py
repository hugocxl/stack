from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import photo_print

DESCRIPTION = "A landscape print carries a ribboned certificate seal with a lock at its lower corner."


def draw(s):
    print_ = photo_print(s, 94, 73, angle=-12)
    print_.slab([(70, 55), (82, 60), (79, 81), (72, 76), (66, 80)], 2, EDGE)
    print_.slab([(85, 57), (94, 55), (103, 77), (96, 75), (93, 81)], 2, EDGE)
    badge(s, "lock", *print_.at(88, 58), 17)
