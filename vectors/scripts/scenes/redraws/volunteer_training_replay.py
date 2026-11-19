from geometry import BOLD, EDGE
from scenes.redraws._w3 import printed_glyph, video_device

DESCRIPTION = "An open laptop shows a training video with a replay arrow surrounding the play control."


def draw(s):
    screen = video_device(s)
    printed_glyph(screen, "refresh", 56, 40, 33, BOLD)
    printed_glyph(screen, "play", 56, 36, 12, EDGE)
    screen.rules(16, 13, [80])
    screen.oval(34, 13, 1.8, 1.8, EDGE)
