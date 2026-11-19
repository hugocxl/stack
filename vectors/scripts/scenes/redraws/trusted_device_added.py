from geometry import BOLD
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import device

DESCRIPTION = "A smartphone with a lock on its screen carries an approval check badge on its upper corner."


def draw(s):
    face = device(s, w=43, h=66)
    glyph(s, "lock", *face(21.5, 33), 20, BOLD)
    badge(s, "check", *face(42, 54), 12.4)
