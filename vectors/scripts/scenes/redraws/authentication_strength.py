from geometry import EDGE
from scenes.redraws._w5 import rect, trust_padlock

DESCRIPTION = "A closed padlock has three ascending meter bars inset into its face."


def draw(s):
    trust_padlock(s, keyway=False, shackle_height=23)
    face = lambda x, z: (x, 23, z)
    for x, height in ((10, 5), (20, 11), (30, 17)):
        rect(s, face, x, 4.5, 7, height, 1, EDGE)
