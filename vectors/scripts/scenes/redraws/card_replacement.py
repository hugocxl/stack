from scenes.redraws._kit import badge
from scenes.redraws._w5 import payment_card

DESCRIPTION = "An outward arrow badge points from the edge of an older payment card to the overlapping replacement card."


def draw(s):
    payment_card(s, z=12, back=True)
    face = payment_card(s, x=24, y=6)
    badge(s, "arrow", *face(34, 46), 11)
