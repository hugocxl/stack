from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import van

DESCRIPTION = "A fleet van has a forward dispatch arrow extending from its front bumper."


def draw(s):
    van(s)
    arrow(s, [(73, 14, 11), (106, 14, 11)], BOLD, head=10)
