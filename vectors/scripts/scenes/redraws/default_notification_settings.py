from scenes.redraws._kit import _screen, badge
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A flared notification bell carries a refresh badge for restoring its default settings."


def draw(s):
    notification_bell(s)
    badge(s, "refresh", *_screen(0, 0, 0, 33, 9), 12.6)
