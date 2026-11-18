from scenes.redraws._kit import badge
from scenes.redraws._w5 import identity_card, identity_details

DESCRIPTION = "A standing profile card carries a plus badge beside its portrait and profile lines."


def draw(s):
    face = identity_card(s)
    identity_details(s, face)
    badge(s, "plus", *face(67, 40), 13)
