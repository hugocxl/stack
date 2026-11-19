from scenes.redraws._w1 import exchange_arrows, profile_card

DESCRIPTION = "Two overlapping profile cards carry a pair of opposed arrows at their upper corners."


def draw(s):
    profile_card(s, -49, -8, 17)
    profile_card(s, -24, 8, 0)
    exchange_arrows(s, 33, 1, 48, 27)
