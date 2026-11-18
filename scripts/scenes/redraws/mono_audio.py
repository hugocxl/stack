from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A single loudspeaker shows one centered waveform strip beneath its cone."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 65, 79, 5), 26)
    face.oval(32.5, 48, 23, 23, EDGE)
    face.oval(32.5, 48, 17, 17, DETAIL)
    face.oval(32.5, 48, 7, 7, EDGE)
    face.rect(10, 7, 45, 15, 2)
    face.stroke([(14, 14), (20, 14), (23, 17), (26, 11), (30, 20),
                 (33, 9), (37, 18), (41, 12), (45, 14), (51, 14)], BOLD)
