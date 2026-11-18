from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import payment_card

DESCRIPTION = "A curved arrow returns across the face of a payment card and points back toward its chip."


def draw(s):
    face = payment_card(s)
    path = [face(x, z) for x, z in oval(42, 24, 15, 11, -110, 155, 32)]
    arrow(s, path + [face(28, 25)], BOLD, head=7)
