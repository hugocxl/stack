from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import podium_art, video_device

DESCRIPTION = "An open laptop displays a keynote lectern with a playback bar and a play badge."


def draw(s):
    screen = video_device(s)
    podium_art(screen, 51, 41, 38)
    screen.rules(16, 14, [77], ink=EDGE)
    screen.oval(32, 14, 2.6, 2.6, EDGE)
    badge(s, "play", *screen.point(106, 25), 17)
