from scenes.redraws._kit import glyph
from scenes.redraws._w1 import software_package

DESCRIPTION = "A downward download arrow marks the front of a sealed release package."


def draw(s):
    software_package(s, 0, 0, 0, show_code=False)
    glyph(s, "down", 0, 21, 16, 16)
