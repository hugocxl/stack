from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import ruled_file

DESCRIPTION = "A paperclipped document carries a check badge at its lower corner."


def attachment(s):
    face = ruled_file(s)
    clip = [(9, 46), *oval(16, 53, 7, 6, 180, 0, 18),
            *oval(18.5, 39, 4.5, 4.5, 0, -180, 18), (14, 50)]
    s.tube([face(x, z) for x, z in clip], 1.03, EDGE)
    return face(46, 6)


def draw(s):
    badge(s, "check", *attachment(s), 12)
