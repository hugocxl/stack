from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph, speaker_art

DESCRIPTION = "A raised read-aloud toolbar pairs a loudspeaker with a play button and an integrated progress track."


def draw(s):
    toolbar = Surface(s, (0, 22, 0), rise=(-.61, .79), back=(0, -.79, -.61))
    toolbar.plate(rounded(0, 0, 109, 52, 8), 12)
    toolbar.stroke([(46, 9), (46, 43)], EDGE)
    speaker_art(toolbar, 25, 26, 29, EDGE)
    toolbar.rect(53, 23, 29, 22, 6, EDGE)
    printed_glyph(toolbar, "play", 67.5, 34, 12, BOLD)
    toolbar.rules(55, 13, [44], ink=EDGE)
    toolbar.oval(73, 13, 3, 3, EDGE)
