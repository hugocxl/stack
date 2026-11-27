from scenes.redraws._kit import badge
from scenes.redraws._sf import BACK, left_face, plate, squircle

DESCRIPTION = "An upright ribbed suitcase with a pull handle carries a refresh badge for recheck."


def draw(s):
    from geometry import DETAIL, EDGE
    for x in (-14, 14):
        s.tube([(x, 6, 70), (x, 6, 92)], 1.8, EDGE)
    s.tube([(-14, 6, 92), (14, 6, 92)], 2.4, EDGE)
    for x in (-18, 18):
        s.disk(x, 16, 0, 4, 4, 4)
    face = left_face(-28, 26, 4)
    plate(s, face, squircle(56, 70, 10), 22, (0, -1, 0))
    for u in (16, 28, 40):
        s.line([face(u, 8), face(u, 62)], DETAIL)
    badge(s, "refresh", 28, 26, 10, 13)
