from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import ruled_file

DESCRIPTION = "A document with a large paperclip carries an X badge on its lower corner."


def draw(s):
    face = ruled_file(s)
    clip = [(8, 38), (8, 50), (9, 55), (12, 57), (16, 57),
            (19, 54), (19, 45), (17, 42), (14, 42), (12, 44), (12, 51)]
    s.tube([face(x, z) for x, z in clip], .85, EDGE)
    badge(s, "x", 45, 1, 7, 12)
