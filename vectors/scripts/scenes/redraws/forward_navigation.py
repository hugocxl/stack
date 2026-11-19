from geometry import BOLD
from scenes.redraws._w4 import upright

DESCRIPTION = "A broad right-pointing navigation arrow has a clean head and shallow isometric depth."


def draw(s):
    upright(s, [(0, 17), (53, 17), (53, 0), (85, 27), (53, 54),
                (53, 37), (0, 37)], 0, 8, BOLD, angle=-20)
