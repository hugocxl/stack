from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two audio level meters reach the same bold target rule inside one stereo meter."


def draw(s):
    meter = Surface(s, (0, 0, 0), rise=(-.24, .97), back=(0, -.97, -.24))
    meter.plate(rounded(0, 0, 92, 73, 5), 21)
    meter.rect(8, 8, 76, 57, 3, EDGE)
    for x, levels in ((23, (13, 21, 29, 37)), (55, (13, 25, 35))):
        meter.rect(x - 2, 10, 18, 50, 2, DETAIL)
        for low, high in zip(levels, (*levels[1:], 45)):
            meter.rect(x, low, 14, high - low - 2, 1, EDGE)
        meter.rules(x + 1, 54, [12], ink=DETAIL)
    meter.rules(13, 47, [66], ink=BOLD)
    for x in (13, 79):
        meter.stroke([(x, 44), (x, 50)], BOLD)
