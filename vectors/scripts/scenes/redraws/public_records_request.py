from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import clipboard, task_rows

DESCRIPTION = "A records request clipboard has an archive-folder emblem and a clock badge."


def draw(s):
    clipboard(s)
    s.face([(-15, 0, 24), (-15, 0, 39), (-5, 0, 39), (-1, 0, 35),
            (14, 0, 35), (14, 0, 24)], EDGE)
    s.line([(-15, .1, 24), (-9, .1, 32), (17, .1, 32), (14, .1, 24)], EDGE)
    task_rows(s, (-18, 15, 30), (-18, 6, 24))
    badge(s, "clock", 29, -1, 37, 10.5)
