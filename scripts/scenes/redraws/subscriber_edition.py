from scenes.redraws._kit import badge
from scenes.redraws._w4 import magazine

DESCRIPTION = "A bound magazine with a landscape on its cover carries a lock badge at the outer edge."


def draw(s):
    cover = magazine(s)
    badge(s, "lock", *cover.at(78, 80), 18)
