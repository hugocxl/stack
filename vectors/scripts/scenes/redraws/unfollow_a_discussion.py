from scenes.redraws._kit import badge
from scenes.redraws.follow_a_discussion import discussion_bell

DESCRIPTION = "A thick discussion bubble with two lines of text carries a slash badge for unfollowing."


def draw(s):
    badge(s, "slash", *discussion_bell(s), 14)
