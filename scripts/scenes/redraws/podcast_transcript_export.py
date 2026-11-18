from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, microphone

DESCRIPTION = "A transcript page has a microphone header, rows of dialogue, and an outward arrow badge."


def draw(s):
    page = Surface(s, (0, 58, 5), rise=(-.54, .84), back=(0, -.84, -.54))
    page.plate([(0, 0), (75, 0), (75, 79), (59, 95), (0, 95)], 5)
    page.stroke([(59, 95), (59, 79), (75, 79)], EDGE)
    microphone(page, 19, 70, 21, EDGE)
    page.rules(33, 76, (21, 16), gap=7, ink=BOLD)
    for v, widths in ((47, (37, 31)), (28, (39, 26)), (10, (38,))):
        page.rules(11, v, (4,), ink=EDGE)
        page.rules(22, v, widths, gap=6)
    badge(s, "arrow", *page.point(74, 43), 14)
