from scenes.redraws.message_delivered import message
from scenes.redraws.notifications_grouped import bell_badge

DESCRIPTION = "A rounded comment bubble with three short lines carries a bell badge."


def draw(s):
    bell_badge(s, message(s), 13)
