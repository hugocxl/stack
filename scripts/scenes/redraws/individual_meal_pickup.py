from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import clamshell

DESCRIPTION = "An open single-serving takeaway clamshell has an outward arrow extending from its front latch."


def draw(s):
    clamshell(s, opened=True)
    arrow(s, [(24, 36, 11), (24, 56, 11)], BOLD, head=8)
