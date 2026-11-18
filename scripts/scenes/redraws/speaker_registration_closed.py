from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, microphone

DESCRIPTION = "A lanyard credential with a microphone emblem has a lock badge at its lower corner."


def draw(s):
    loop = oval(32, 97, 19, 25, 245, -65, count=36)
    s.tube([(x, -.48 * (z - 73), z) for x, z in loop], 2.5)
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 64, 85, 6), 6)
    face.rect(21, 73, 22, 6, 2, EDGE)
    face.rect(8, 9, 48, 56, 3)
    microphone(face, 32, 46, 25)
    face.rules(20, 21, [24, 18], gap=6)
    badge(s, "lock", 62, 0, 13, 14)
