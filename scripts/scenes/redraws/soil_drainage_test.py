from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow

DESCRIPTION = "A soil cross-section exposes a water-filled test hole and downward seepage into the layer beneath it."


def draw(s):
    left, right, front, top = -43, 43, 24, 47
    bank = [(left, front, 0), (right, front, 0), (right, front, top),
            (19, front, top), (16, front, 25), (10, front, 20),
            (-9, front, 20), (-16, front, 25), (-18, front, top), (left, front, top)]
    s.face([(right, -33, 0), (right, front, 0), (right, front, top), (right, -33, top)])
    rim = oval(.5, front, 18.5, 26, 180, 360, 60)
    top_face = [(left, -33), (right, -33), (right, front), *reversed(rim), (left, front)]
    s.face([(x, y, top) for x, y in top_face])
    water = oval(.5, front, 16.4, 19, 180, 360, 48)
    s.face([(x, y, 31) for x, y in water], EDGE)
    s.line([(-9, 19, 31), (-3, 18, 31), (4, 19, 31)], DETAIL)
    s.face(bank)
    s.line([(-16, front + .1, 31), (17, front + .1, 31)], EDGE)
    for x in (-9, 0, 9):
        arrow(s, [(x, front + .1, 16), (x, front + .1, 5 if x else 3)], EDGE, head=3.2)
    for x, z in ((-34, 10), (-34, 32), (-26, 20), (-23, 6), (24, 14), (33, 32), (34, 8)):
        s.line([(x, front + .1, z), (x + 4, front + .1, z + 1)], DETAIL)
    s.line([(27, front + .1, 26), (34, front + .1, 25), (43, front + .1, 27),
            (43, 0, 26), (43, -14, 29), (43, -33, 26)], DETAIL)
