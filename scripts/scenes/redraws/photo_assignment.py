from geometry import EDGE
from scenes.redraws._w3 import clipboard
from scenes.redraws._w4 import Surface, camera_emblem

DESCRIPTION = "A clipped assignment sheet displays a large camera pictogram above two short instruction lines."


def draw(s):
    sheet = clipboard(s, w=79, h=93)
    camera_emblem(Surface(s, lambda u, v: sheet.point(u, 88 - v)), 16, 24, 46)
    sheet.rules(17, 22, (40, 28), gap=7, ink=EDGE)
