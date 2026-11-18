from scenes.redraws._kit import _screen, badge
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A flared notification bell carries a minus badge on its lower-right rim."


def draw(s):
    notification_bell(s)
    badge(s, "minus", *_screen(0, 0, 0, 33, 9), 12.6)
