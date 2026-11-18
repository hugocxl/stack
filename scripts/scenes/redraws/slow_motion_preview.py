from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import play_mark, video_player

DESCRIPTION = "A video player shows a play symbol and a playback-speed dial set in the lower half of its range."


def draw(s):
    player = video_player(s)
    play_mark(player, 50, 30, 12)
    player.slab(rounded(87, 37, 42, 42, 7), 5)
    player.oval(108, 58, 15, 15, EDGE)
    player.line([(96, 61), (97, 55), (102, 50), (108, 49), (114, 50),
                 (119, 55), (120, 61)], DETAIL)
    player.line([(108, 62), (101, 54)], BOLD)
    player.oval(108, 62, 2.2, 2.2, EDGE)
