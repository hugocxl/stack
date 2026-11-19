from geometry import BOLD, EDGE
from scenes.redraws._w1 import software_package
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A sealed carton bears a code mark on the front and an equals sign on its side label."


def draw(s):
    software_package(s, 0, 0, 0)
    label = Surface(s, (29, 21, 0), across=(0, -1))
    label.rect(9, 6, 24, 23, 2, EDGE)
    for z in (14, 21):
        printed_glyph(label, "minus", 21, z, 9, BOLD)
