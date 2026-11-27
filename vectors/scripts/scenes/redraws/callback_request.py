from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import handset, screen

DESCRIPTION = "A telephone handset carries a clock badge for a scheduled call back."


def draw(s):
    handset(s, screen())
    badge(s, "clock", *_screen(0, 0, 0, 26, 22), 14)
