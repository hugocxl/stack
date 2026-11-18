from geometry import EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import Surface

DESCRIPTION = "A dressing-room door has a large star plaque above its lever handle."


def draw(s):
    frame = Surface(s, (0, 0, 0))
    frame.plate(rounded(0, 0, 64, 105, 2), 13)
    frame.rect(5, 3, 54, 97, 1, EDGE)
    frame.rect(12, 14, 40, 34, 2)
    frame.rect(14, 55, 36, 35, 4, EDGE)
    glyph(s, "star", 32, 0, 72, 17)
    frame.oval(51, 48, 3.3, 3.3)
    frame.stroke([(51, 48), (42, 48)], EDGE)
    frame.stroke([(4, 2), (60, 2)], EDGE)
