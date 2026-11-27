from geometry import DETAIL, EDGE
from scenes.redraws._sf import bolt, left_face, plate, squircle

DESCRIPTION = "A home battery is mounted on a wall above a dashed floor clearance."


def draw(s):
    wall = left_face(-50, 0, 0)
    plate(s, wall, [(0, 0), (100, 0), (100, 96), (0, 96)], 4, (0, -1, 0))
    s.line([(-50, 4, 0), (-50, 40, 0)], DETAIL)
    s.line([(50, 4, 0), (50, 40, 0)], DETAIL)
    s.line([(-30, 30, 0), (30, 30, 0)], DETAIL, dashed=True)
    s.line([(-30, 4, 0), (-30, 30, 0)], DETAIL, dashed=True)
    s.line([(30, 4, 0), (30, 30, 0)], DETAIL, dashed=True)
    body = left_face(-24, 18, 30)
    plate(s, body, squircle(48, 58, 8), 14, (0, -1, 0))
    bolt(s, lambda u, v: body(24 + u, 36 + v), 9)
    for i in range(4):
        s.line([body(14 + i*6.5, 14), body(18 + i*6.5, 14)], EDGE if i < 3 else DETAIL)
