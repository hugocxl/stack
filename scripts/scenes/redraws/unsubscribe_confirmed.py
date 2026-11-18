from scenes.redraws._kit import _screen, badge
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A flared notification bell carries an X badge on its lower-right rim."


def draw(s):
    notification_bell(s)
    badge(s, "x", *_screen(0, 0, 0, 33, 9), 12.6)
