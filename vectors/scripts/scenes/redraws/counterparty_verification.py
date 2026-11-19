from scenes.redraws._kit import badge
from scenes.redraws._w5 import identity_card, identity_details

DESCRIPTION = "An identity card carries a check badge at the upper corner of its portrait frame."


def draw(s):
    face = identity_card(s)
    identity_details(s, face)
    badge(s, "check", *face(35, 42), 9.5)
