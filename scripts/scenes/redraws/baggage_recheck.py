from geometry import EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import luggage

DESCRIPTION = "A curved return arrow loops around the top handle of an upright suitcase."


def draw(s):
    luggage(s)
    arc = oval(26, 9, 26, 16, 14, 297, 34)
    arrow(s, [(x, y, 65) for x, y in arc], EDGE, head=7)
