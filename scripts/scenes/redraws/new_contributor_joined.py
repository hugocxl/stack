from scenes.redraws._kit import badge
from scenes.redraws._w2 import identification_card

DESCRIPTION = "Three clipped ID cards fan together, with a check badge attached to the newest card."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x - .25*z, .90*z

    for offset, lift in ((0, 10), (23, 16), (48, 0)):
        def card(u, v):
            return point(u + offset, v + lift)

        identification_card(s, card)
    badge(s, "check", *point(101, 65), 14)
