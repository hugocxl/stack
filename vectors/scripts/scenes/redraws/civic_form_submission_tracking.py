from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import clipboard, task_rows

DESCRIPTION = "A civic form on a standing clipboard has a three-stop progress track along its edge."


def draw(s):
    clipboard(s)
    s.line([(-21, 0, 32), (-21, 0, 37), (-9, 0, 42), (3, 0, 37),
            (3, 0, 32), (-21, 0, 32)], EDGE)
    s.line([(-21, 0, 37), (3, 0, 37)], DETAIL)
    for x in (-16, -9, -2):
        s.line([(x, 0, 33), (x, 0, 36)], DETAIL)
    task_rows(s, (-21, 23, 15), (-21, 15, 12), (-21, 7, 14))
    x, y = 15, 0
    for z in (13, 26, 39):
        s.face([(a, y, b) for a, b in oval(x, z, 3.6, 3.6, count=24)[:-1]], EDGE)
    s.line([(x, y, 16.6), (x, y, 22.4)], BOLD)
    s.line([(x, y, 29.6), (x, y, 35.4)], DETAIL)
    s.line([(a, y, b) for a, b in oval(x, 26, 1.55, 1.55, count=20)], BOLD)
