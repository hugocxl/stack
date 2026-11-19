from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import play_mark, video_player

DESCRIPTION = "A video player has a closed-caption control marked by two lines in a small speech bubble."


def draw(s):
    player = video_player(s)
    play_mark(player, 54, 31, 13)
    player.slab(rounded(94, 52, 32, 28, 5), 4)
    player.outline([(100, 59), (120, 59), (120, 70), (111, 70),
                    (106, 74), (106, 70), (100, 70)], EDGE)
    player.rows(103, 63, (13, 9), step=4, ink=BOLD)
