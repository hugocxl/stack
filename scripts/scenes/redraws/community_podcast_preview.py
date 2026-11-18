from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A broadcast microphone in a desk stand carries a play badge below its grille."


def draw(s):
    s.disk(0, 0, 0, 24, 17, 5)
    s.disk(0, 0, 5, 3.3, 3.3, 23)
    yoke = Surface(s, (0, 2, 0))
    s.tube([yoke.point(x, v) for x, v in [(-24, 55), (-24, 46), (-21, 37),
           (-15, 30), (-7, 26), (7, 26), (15, 30), (21, 37), (24, 46), (24, 55)]], 2)
    face = Surface(s, (0, 11, 0))
    face.plate(rounded(-17, 35, 34, 60, 17), 17)
    for v, width in ((84, 16), (76, 23), (68, 23), (60, 20)):
        face.rules(-width / 2, v, [width], ink=EDGE)
    s.tube([face.point(-22, 54, 5), face.point(-16, 54, 5)], 2.7)
    s.tube([face.point(16, 54, 5), face.point(22, 54, 5)], 2.7)
    badge(s, "play", 16, 15, 41, 12)
