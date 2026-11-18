from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, podium_art

DESCRIPTION = "A slotted event pass shows a session lectern and carries a forward arrow at its right edge."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 68, 84, 6), 6)
    face.rect(24, 70, 20, 5, 2, EDGE)
    podium_art(face, 32, 47, 28)
    face.rules(12, 24, [33], ink=EDGE)
    face.rules(12, 15, [27])
    badge(s, "arrow", 69, 0, 33, 16)
