from geometry import BOLD
from scenes.redraws._w4 import molar, upright

DESCRIPTION = "A single molar has a broad, rounded crown and two separated tapered roots."


def draw(s):
    upright(s, molar(0, 0), 0, 9, BOLD, angle=-24)
