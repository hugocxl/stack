from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import card_terminal, currency_mark, panel, printed_stroke, rect

DESCRIPTION = "A dollar banknote stands behind a payment terminal with a chip card inserted below its keypad."


def draw(s):
    banknote = lambda x, z: (x, 1 + .24 * x, z)
    panel(s, rounded(-13, 4, 51, 46, 2), banknote, 2)
    rect(s, banknote, -8, 9, 41, 36, 1, DETAIL)
    printed_stroke(s, banknote, oval(11, 34, 10, 9), EDGE)
    currency_mark(s, banknote, 11, 34, 7, ink=BOLD)
    card_terminal(s)
    card = lambda x, y: (x, y, 4.4)
    s.face([card(x, y) for x, y in rounded(8, 61, 33, 20, 2.5)])
    rect(s, card, 14, 67, 8, 7, 1.3, EDGE)
