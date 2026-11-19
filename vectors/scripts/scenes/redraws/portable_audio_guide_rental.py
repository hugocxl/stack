from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import printed_glyph
from scenes.redraws.gallery_tour_listening_station import handset

DESCRIPTION = "A handheld museum audio guide has an earpiece grille and an attached clock badge."


def draw(s):
    face = handset(s)
    printed_glyph(face, "play", 23, 20, 6, EDGE)
    badge(s, "clock", 49, -4, 59, 14)
