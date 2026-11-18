from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A lock badge overlaps the upper corner of a framed mountain painting."


def draw(s):
    frame = Surface(s, (0, 0, 0), rise=(-.18, .98), back=(0, -.98, -.18))
    frame.plate(rounded(0, 0, 89, 72, 2), 10)
    frame.rect(6, 6, 77, 60, 1, EDGE)
    frame.rect(11, 11, 67, 50, 1)
    frame.stroke([(12, 19), (29, 40), (40, 27), (58, 48), (77, 23)], BOLD)
    frame.stroke([(51, 40), (58, 42), (63, 40)])
    frame.oval(27, 50, 4, 4)
    badge(s, "lock", *frame.point(85, 64, -2), 16)
