from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, microphone

DESCRIPTION = "An archival cassette bears a microphone emblem and the waveform of a recorded interview."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.34, .94), back=(0, -.94, -.34))
    face.plate(rounded(0, 0, 108, 70, 6), 16)
    face.rect(7, 11, 94, 53, 4, EDGE)
    face.rect(28, 13, 55, 22, 8, EDGE)
    for x in (39, 72):
        face.oval(x, 24, 7.5, 7.5, EDGE)
        face.oval(x, 24, 3.5, 3.5)
    face.rules(47, 26, [17])
    face.rules(47, 22, [17])
    face.stroke([(14, 0), (20, 9), (87, 9), (94, 0)], EDGE)
    microphone(face, 23, 49, 24)
    face.stroke([(42, 49), (47, 49), (51, 55), (55, 43), (59, 53), (63, 40),
                 (68, 59), (73, 46), (77, 51), (81, 44), (86, 51), (93, 49)], BOLD)
