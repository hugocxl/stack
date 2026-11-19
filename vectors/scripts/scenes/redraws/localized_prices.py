from geometry import BOLD, EDGE, oval
from scenes.redraws._w3 import Surface

DESCRIPTION = "An upright price tag shows two aligned price rows marked with euro and yen signs."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.26, .97), back=(0, -.97, -.26),
                   across=(.94, -.34))
    face.plate([(0, 4), (4, 0), (86, 0), (90, 4), (90, 76),
                (76, 92), (14, 92), (0, 76)], 9)
    face.oval(45, 81, 4, 4)
    face.stroke([(9, 41), (81, 41)])
    euro = face.viewer_axes(22, 61)
    face.stroke([euro(x, v) for x, v in oval(0, 0, 7, 9, 50, 310, 24)], BOLD)
    for v in (-2, 2):
        face.stroke([euro(-6, v), euro(1, v)], BOLD)
    yen = face.viewer_axes(22, 23)
    face.stroke([yen(-6, 8), yen(0, 1), yen(6, 8)], BOLD)
    face.stroke([yen(0, 1), yen(0, -8)], BOLD)
    for v in (0, -4):
        face.stroke([yen(-5, v), yen(5, v)], BOLD)
    for v in (60, 23):
        face.rules(38, v, [33], ink=EDGE)
        face.rules(38, v - 5, [19])
