from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import software_package

DESCRIPTION = "An upward arrow launches from the top of a sealed software carton."


def draw(s):
    software_package(s, 0, 0, 0)
    arrow(s, [(13, 0, 36), (13, 0, 86)], BOLD, head=14)
