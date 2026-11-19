from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w5 import bank_mark, currency_mark, panel, printed_stroke, rect

DESCRIPTION = "A thick calculator shows a treasury emblem and an estimated currency amount above its keypad."


def draw(s):
    face = lambda x, z: (x, -.70 * z, z)
    panel(s, rounded(0, 0, 57, 64, 5), face, 13)
    rect(s, face, 6, 38, 45, 19, 3, EDGE)
    bank_mark(s, face, 17, 47, .72)
    currency_mark(s, face, 33, 47, 5.5, ink=BOLD)
    printed_stroke(s, face, [(40, 47), (46, 47)], EDGE)
    for z in (8, 18, 28):
        for x in (8, 19, 30, 41):
            rect(s, face, x, z, 7.5, 6.5, 1.5, DETAIL)
