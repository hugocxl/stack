from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import payment_card, printed_stroke

DESCRIPTION = "An upward arrow rises from the credit-limit line on a chipped payment card."


def draw(s):
    face = payment_card(s)
    printed_stroke(s, face, [(35, 21), (61, 21)], EDGE)
    arrow(s, [face(52, 21), face(52, 37)], BOLD, head=7)
