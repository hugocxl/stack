from scenes.redraws._kit import badge
from scenes.redraws.attachment_delivered import attachment

DESCRIPTION = "A paperclipped document carries an upward arrow badge at its lower corner."


def draw(s):
    badge(s, "up", *attachment(s), 12)
