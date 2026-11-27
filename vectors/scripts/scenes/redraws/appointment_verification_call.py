from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import handset, screen

DESCRIPTION = "A telephone handset carries a check badge beside its upper earpiece."


def draw(s):
    handset(s, screen())
    badge(s, "check", *_screen(0, 0, 0, 26, 22), 14)
