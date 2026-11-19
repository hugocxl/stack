from scenes.redraws._kit import badge
from scenes.redraws._w5 import device, shield_mark

DESCRIPTION = "A smartphone with a shield on its screen carries an x badge at its lower corner."


def draw(s):
    face = device(s)
    shield_mark(s, face, 19, 35, 24)
    badge(s, "x", *face(37, 11), 11)
