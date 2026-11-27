from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import handset, screen

DESCRIPTION = "A telephone handset carries a return badge asking for a call back."


def draw(s):
    handset(s, screen())
    badge(s, "back", *_screen(0, 0, 0, 26, 22), 14)
