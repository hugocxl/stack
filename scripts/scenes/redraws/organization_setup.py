from scenes.redraws._kit import badge
from scenes.redraws._w1 import organization_card

DESCRIPTION = "A plus badge overlaps the upper corner of an organization profile card with a printed office tower."


def draw(s):
    organization_card(s)
    badge(s, "plus", 37, 0, 50, 12)
