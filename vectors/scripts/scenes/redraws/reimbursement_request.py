from scenes.redraws._kit import badge
from scenes.redraws._w5 import expense_receipt

DESCRIPTION = "An itemized expense receipt has a clock badge attached beside its ruled currency total."


def draw(s):
    face = expense_receipt(s)
    badge(s, "clock", *face(56, 18), 12)
