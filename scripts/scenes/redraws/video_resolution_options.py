from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import landscape, video_player

DESCRIPTION = "A video player has an attached selector with two visibly different picture sizes."


def draw(s):
    player = video_player(s)
    landscape(player, 13, 13, 60, 34)
    player.slab(rounded(80, 13, 57, 46, 4), 4)
    player.line([(81, 36), (136, 36)], EDGE)
    player.frame(92, 21, 15, 9, 1, EDGE)
    player.frame(89, 41, 21, 13, 1, BOLD)
    player.line([(120, 26), (126, 26)])
    player.line([(118, 48), (128, 48)], EDGE)
