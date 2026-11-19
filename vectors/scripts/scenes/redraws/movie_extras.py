from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import play_mark, video_player

DESCRIPTION = "A movie thumbnail with perforated film edges and a play symbol carries a plus badge."


def draw(s):
    player = video_player(s)
    for u in (15, 32, 49, 66, 83, 100):
        for v in (11, 45):
            player.frame(u - 3, v, 6, 3.5, .7, EDGE)
    player.line([(8, 18), (107, 18)], DETAIL)
    player.line([(8, 41), (107, 41)], DETAIL)
    play_mark(player, 57, 30, 11, EDGE)
    badge(s, "plus", *player.at(115, 11), 17)
