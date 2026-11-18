from geometry import BOLD
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import ticket

DESCRIPTION = "A perforated gala ticket has a large engraved heart beside its stub."


def draw(s):
    face = ticket(s)
    glyph(s, "heart", 38, 0, 25, 22, BOLD)
    face.rules(20, 7, [36])
