from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, speech_outline

DESCRIPTION = "A field recorder has a built-in microphone, a speech label and a waveform on its display."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.25, .97), back=(0, -.97, -.25))
    face.plate(rounded(10, 63, 34, 29, 12), 12)
    for v, width in ((85, 20), (80, 24), (75, 24)):
        face.rules(27 - width / 2, v, [width], ink=EDGE)
    face.plate(rounded(0, 0, 54, 70, 6), 15)
    face.rect(6, 20, 42, 44, 3, EDGE)
    face.stroke(speech_outline(12, 50, 22, 9), EDGE, closed=True)
    face.rules(16, 55, [13], ink=DETAIL)
    face.stroke([(11, 35), (15, 35), (18, 40), (22, 28), (26, 44), (31, 31),
                 (35, 40), (39, 35), (43, 35)], BOLD)
    face.oval(27, 10.5, 4.5, 4.5, EDGE)
    for x in (13, 41):
        face.rules(x - 2, 10.5, [4], ink=DETAIL)
