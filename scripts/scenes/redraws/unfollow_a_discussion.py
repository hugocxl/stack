from scenes.redraws._kit import badge
from scenes.redraws.follow_a_discussion import discussion_bell

DESCRIPTION = "A slash badge overlaps the shoulder of the notification bell on a discussion bubble."


def draw(s):
    bell = discussion_bell(s)
    badge(s, "slash", *bell(16, 5), 12)
