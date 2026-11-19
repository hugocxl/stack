from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import play, video_device

DESCRIPTION = "A laptop shows a recorded video with a play triangle, scrubber, and replay badge."


def draw(s):
    screen = video_device(s)
    play(screen, 53, 41, 27)
    screen.rules(12, 15, [85], ink=DETAIL)
    screen.rules(12, 15, [25], ink=EDGE)
    screen.oval(38, 15, 2.5, 2.5, EDGE)
    badge(s, "refresh", *screen.point(105, 9), 13)
