from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, play, printed_glyph

DESCRIPTION = "A video player has a play triangle and a slash badge across its lightning control."


def draw(s):
    player = Surface(s, (0, 0, 0), rise=(-.21, .98), back=(0, -.98, -.21))
    player.plate(rounded(0, 0, 104, 74, 7), 11)
    player.rect(7, 23, 90, 44, 3, EDGE)
    play(player, 51, 44, 25, EDGE, aligned=True)
    player.rules(9, 13, [58], ink=EDGE)
    player.oval(28, 13, 2.8, 2.8, EDGE)
    player.rect(68, 4, 29, 17, 3, EDGE)
    printed_glyph(player, "bolt", 77, 13, 9, EDGE)
    badge(s, "slash", *player.point(96, 7, -3), 12)
