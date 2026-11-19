from scenes.redraws._w5 import identity_card, identity_details

DESCRIPTION = "A standing ID card shows a large portrait outline and two short identity lines."


def draw(s):
    identity_details(s, identity_card(s))
