from geometry import DETAIL, EDGE
from scenes.redraws._sf import left_face, plate

DESCRIPTION = "An illustrated issue rises out of an open envelope."


def draw(s):
    w, h = 100, 60
    # The back of the open envelope.
    back = left_face(0, 0, 0)
    plate(s, back, [(0, 0), (w, 0), (w, h), (0, h)], 3, (0, -1, 0))
    # The issue stands inside.
    page = left_face(12, 3, 18)
    plate(s, page, [(0, 0), (w - 24, 0), (w - 24, 70), (0, 70)], 2, (0, -1, 0))
    s.line([page(u, v) for u, v in [(8, 48), (24, 62), (36, 52), (48, 64), (68, 46)]], EDGE)
    for v, width in ((38, 58), (30, 46), (22, 52)):
        s.line([page(8, v), page(8 + width, v)], DETAIL)
    # The front pocket of the envelope, cut in a shallow V.
    front = left_face(0, 6, 0)
    plate(s, front, [(0, 0), (w, 0), (w, h*.62), (w/2, h*.3), (0, h*.62)], 3, (0, -1, 0))
