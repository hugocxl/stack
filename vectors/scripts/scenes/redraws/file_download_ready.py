from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import ruled_file

DESCRIPTION = "A document has a large download arrow extending down from its lower edge."


def draw(s):
    ruled_file(s)
    arrow(s, [(27, 1, 8), (27, 1, -17)], BOLD, head=8.5)
