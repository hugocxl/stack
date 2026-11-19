from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import currency_mark, device, printed_stroke, rect

DESCRIPTION = "A smartphone camera frames a bank check with a currency amount and a signature line."


def draw(s):
    face = device(s, w=54, h=81)
    rect(s, face, 8, 31, 38, 24, 1.2)
    currency_mark(s, face, 34, 44, 4, ink=EDGE)
    printed_stroke(s, face, [(39, 44), (43, 44)], EDGE)
    printed_stroke(s, face, [(11, 50), (25, 50)], DETAIL)
    printed_stroke(s, face, [(11, 43), (24, 43)], DETAIL)
    printed_stroke(s, face, [(11, 36), (21, 36)], DETAIL)
    printed_stroke(s, face, [(29, 36), (33, 39), (35, 36), (42, 36)], EDGE)
    for x, sign_x in ((6.5, 1), (47.5, -1)):
        for z, sign_z in ((27, 1), (59, -1)):
            printed_stroke(s, face, [(x + sign_x * 6, z), (x, z), (x, z + sign_z * 5)], BOLD)
    rect(s, face, 21, 12, 12, 8, 4, EDGE)
