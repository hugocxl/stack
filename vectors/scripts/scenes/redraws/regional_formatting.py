from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two rows on a locale display swap comma and point separators between aligned groups of digit positions."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.22, .98), back=(0, -.98, -.22),
                   across=(.96, -.28))
    face.plate(rounded(0, 0, 106, 91, 6), 11)
    world = face.viewer_axes(24, 73)
    for r in (4, 8):
        face.stroke([world(x, v) for x, v in oval(0, 0, r, 8)], EDGE)
    face.stroke([world(-8, 0), world(8, 0)], EDGE)
    face.rules(40, 73, [41], ink=EDGE)
    for v in (35, 9):
        face.rect(8, v, 90, 20, 3, EDGE)
        for x, height in ((15, 7), (32, 10), (42, 7), (52, 9), (72, 8), (82, 11)):
            face.stroke([(x, v + 7), (x, v + 7 + height), (x + 5, v + 7 + height)], EDGE)
        point, comma = (64, 25) if v == 35 else (25, 64)
        face.oval(point, v + 7, 1.65, 1.65, BOLD)
        face.stroke([(comma + 1.5, v + 10), (comma + 1.5, v + 7),
                     (comma - 1.5, v + 4)], BOLD)
