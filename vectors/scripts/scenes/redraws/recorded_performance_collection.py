from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface
from scenes.redraws.performance_stage_pass import curtain

DESCRIPTION = "A stack of video thumbnails shows stage curtains on the leading card beside a play badge."


def draw(s):
    for x, y, z in ((7, -13, 1), (3, -7, 1), (0, 0, 0)):
        face = Surface(s, (x, y, z), rise=(-.42, .91), back=(0, -.91, -.42))
        face.plate(rounded(0, 0, 94, 63, 5), 3)
    curtain(face, 7, 12, 79, 44)
    face.rules(11, 6, [33], ink=EDGE)
    face.rules(47, 6, [29])
    badge(s, "play", *face.point(91, 17, -3), 12)
