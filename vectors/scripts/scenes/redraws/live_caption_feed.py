from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import landscape, video_player

DESCRIPTION = "A video window shows a bold two-line caption strip inside the bottom of its picture."


def draw(s):
    player = video_player(s)
    landscape(player, 11, 10, 92, 40)
    player.slab(rounded(22, 32, 75, 19, 2), 0, EDGE)
    player.rows(30, 38, (58, 39), step=7, ink=BOLD)
