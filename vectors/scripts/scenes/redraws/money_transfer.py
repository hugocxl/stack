from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import BACK, chevron_arrow, left_face, plate, screen, squircle

DESCRIPTION = "A standing banknote with a printed medallion, and a bold arrow carrying it out to the right."


def draw(s):
    note = left_face(-56, 0, 0)
    plate(s, note, squircle(84, 48, 5), 5, (0, -1, 0))
    s.line([note(u + 6, v + 6) for u, v in squircle(72, 36, 3)] + [note(6, 9.6)], DETAIL)
    s.line([note(42 + a, 24 + b) for a, b in oval(0, 0, 11, 11, count=48)], EDGE)
    for u in (16, 68):
        s.line([note(u + a, 24 + b) for a, b in oval(0, 0, 2.2, 2.2, count=16)], DETAIL)
    at = screen(0, 0, 0)
    plate(s, lambda u, v: at(u + 36, v - 4), chevron_arrow(50, 11, 22), 6, BACK)
