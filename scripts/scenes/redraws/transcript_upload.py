from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A handheld voice recorder displays lines of transcription and carries an upload badge."


def draw(s):
    case = paper(s, 100, pitch=.71, run=.59, angle=12, depth=13)
    case.slab(rounded(0, 0, 53, 100, 11), 13)
    for v, w in ((8, 20), (13, 27), (18, 27)):
        case.rows((53 - w)/2, v, (w,), ink=EDGE)
    case.frame(6, 26, 41, 35, 3, EDGE)
    case.rows(11, 34, (28, 24, 29, 17), step=6)
    case.oval(26, 78, 10, 10, EDGE)
    case.oval(26, 78, 3, 3)
    badge(s, "up", *case.at(54, 44), 16)
