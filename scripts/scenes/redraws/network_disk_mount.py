from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import hard_drive

DESCRIPTION = "An upward mount arrow rises from a disk drive with a keyed network port."


def draw(s):
    hard_drive(s, network=True)
    arrow(s, [(22, -8, 15), (22, -8, 51)], BOLD, head=12)
