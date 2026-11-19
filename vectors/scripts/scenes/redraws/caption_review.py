from geometry import BOLD, EDGE
from scenes.redraws._w4 import landscape, magnifier, video_player

DESCRIPTION = "A video player shows a magnifier over the active line in its caption strip."


def draw(s):
    player = video_player(s)
    landscape(player, 13, 10, 88, 24)
    player.slab([(14, 36), (101, 36), (101, 54), (14, 54)], 0, EDGE)
    player.rows(21, 42, (72,), ink=BOLD)
    player.rows(21, 49, (51,))
    magnifier(player, 65, 44, 13, text=((-2, 14, BOLD), (5, 11, EDGE)))
