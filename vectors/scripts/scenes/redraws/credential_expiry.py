from scenes.redraws._kit import badge
from scenes.redraws._w5 import identity_card, identity_details

DESCRIPTION = "A clock badge overlaps the lower corner of a standing identity credential."


def draw(s):
    face = identity_card(s)
    identity_details(s, face)
    badge(s, "clock", *face(67, 8), 12)
