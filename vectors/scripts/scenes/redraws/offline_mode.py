from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import capsule, left_face, plate, smooth, squircle

DESCRIPTION = "A plug waits a short gap away from its wall socket, its cable trailing behind."


def draw(s):
    socket = left_face(-30, 0, 0)
    plate(s, socket, squircle(60, 60, 14), 6, (0, -1, 0))
    s.line([socket(u + 8, v + 8) for u, v in squircle(44, 44, 9)] + [socket(8, 17)], DETAIL)
    for u in (22, 38):
        slot = [socket(u - 2 + a, 24 + b) for a, b in capsule(4, 12)]
        s.line(slot + slot[:1], BOLD)
    # Cable first, so the plug body hides where it leaves the back.
    s.tube(smooth([(0, 76, 30), (0, 92, 30), (-6, 104, 18), (-22, 108, 3), (-46, 106, 3), (-64, 98, 3)], 6), 3, EDGE)
    for x in (-8, 8):
        s.tube([(x, 50, 30), (x, 30, 30)], 1.7, EDGE)
    body = left_face(-16, 78, 14)
    plate(s, body, squircle(32, 32, 9), 30, (0, -1, 0))
    s.line([body(5, 7), body(27, 7)], DETAIL)
