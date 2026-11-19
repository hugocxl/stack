from scenes.redraws._kit import _screen, badge
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A flared notification bell carries a crescent moon badge at its shoulder."


def draw(s):
    notification_bell(s)
    badge(s, "moon", *_screen(0, 0, 0, 25, 40), 13.6)
