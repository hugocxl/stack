from scenes.redraws._kit import badge
from scenes.redraws._w5 import payment_card

DESCRIPTION = "Two overlapping bank cards share a circular swap-arrow badge."


def draw(s):
    payment_card(s, z=12, bank=True, back=True)
    face = payment_card(s, x=24, y=6, bank=True)
    badge(s, "refresh", *face(44, 43), 11.5)
