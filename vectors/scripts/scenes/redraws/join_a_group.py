from scenes.redraws._kit import _screen, badge
from scenes.redraws.invite_teammates import token

DESCRIPTION = "A close group of three member tokens carries an arrow badge for joining."


def draw(s):
    token(s, -40, 6, 25)
    token(s, 40, 6, 25)
    token(s, 0, 0, 32)
    badge(s, "arrow", *_screen(0, 0, 0, 27, -24), 12)
