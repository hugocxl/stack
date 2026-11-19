from scenes.redraws._w5 import card_terminal

DESCRIPTION = "A countertop payment terminal prints a serrated itemized report from the slot above its display."


def draw(s):
    card_terminal(s, report=True)
