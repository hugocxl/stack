from geometry import BOLD, EDGE
from scenes.redraws._w3 import interface_phone, printed_glyph

DESCRIPTION = "A phone shows a leftward reading arrow above a right-aligned heading and paragraph."


def draw(s):
    phone = interface_phone(s)
    printed_glyph(phone, "back", 23, 62, 16, BOLD)
    phone.rules(19, 47, [17], ink=EDGE)
    for v, length in ((37, 26), (30, 20), (23, 25), (16, 13)):
        phone.rules(36 - length, v, [length], ink=EDGE)
