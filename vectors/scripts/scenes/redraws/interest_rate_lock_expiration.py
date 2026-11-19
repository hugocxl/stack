from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._w5 import lens_outline, printed_stroke, trust_padlock

DESCRIPTION = "A closed padlock has an engraved percent sign and a clock badge on the upper corner of its body."


def draw(s):
    trust_padlock(s, keyway=False)
    face = lambda x, z: (x, 23, z)
    for x, z in ((17, 18), (29, 9)):
        lens_outline(s, face, x, z, 2.9, BOLD)
    printed_stroke(s, face, [(18, 7), (28, 21)], BOLD)
    badge(s, "clock", 48, 21, 26, 10.5)
